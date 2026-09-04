#!/usr/bin/env python3
"""Validate public Draconic integration files without third-party packages."""

from __future__ import annotations

import json
import re
import struct
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MCP_URL = "https://mcp.draconic.ai/mcp"
API_URL = "https://api.draconic.ai"
REQUIRED_JSON = {
    "server.json",
    "mcp.json",
    ".cursor-plugin/plugin.json",
    "configs/cline.mcp.json",
    "postman/Draconic-Intelligence-API.postman_collection.json",
    "postman/Draconic-Intelligence-API.postman_environment.json",
    "submissions/docker/draconic/tools.json",
}
EXPECTED_POSTMAN_PATHS = {
    "/v1/agents/ask",
    "/v1/agents/usage",
    "/v1/agents/coverage?timeframe=5m",
    "/v1/agents/coverage/{{symbol}}?timeframe=multi-timeframe",
}
FORBIDDEN_PATH_NAMES = {".env", "id_rsa", "id_ed25519"}
FORBIDDEN_PATTERNS = {
    "private key": re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
    "Anthropic key": re.compile(r"sk-ant-[A-Za-z0-9_-]{12,}"),
    "OpenAI key": re.compile(r"sk-(?:proj-)?[A-Za-z0-9_-]{20,}"),
    "PostHog key": re.compile(r"phx_[A-Za-z0-9_-]{12,}"),
    "JWT": re.compile(r"eyJ[A-Za-z0-9_-]{10,}\.[A-Za-z0-9_-]{10,}\.[A-Za-z0-9_-]{10,}"),
    "private IPv4 address": re.compile(r"(?:^|[^0-9])(?:10\.\d{1,3}\.\d{1,3}\.\d{1,3}|192\.168\.\d{1,3}\.\d{1,3}|172\.(?:1[6-9]|2\d|3[01])\.\d{1,3}\.\d{1,3})(?:$|[^0-9])"),
    "local endpoint": re.compile(r"https?://(?:localhost|127\.0\.0\.1)(?::\d+)?"),
}


def fail(message: str) -> None:
    print(f"FAIL: {message}", file=sys.stderr)
    raise SystemExit(1)


def json_file(relative: str) -> object:
    path = ROOT / relative
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        fail(f"{relative} is not valid JSON: {exc}")


def check_png(relative: str, expected: tuple[int, int]) -> None:
    data = (ROOT / relative).read_bytes()
    if data[:8] != b"\x89PNG\r\n\x1a\n" or len(data) < 24:
        fail(f"{relative} is not a PNG")
    width, height = struct.unpack(">II", data[16:24])
    if (width, height) != expected:
        fail(f"{relative} is {width}x{height}; expected {expected[0]}x{expected[1]}")


def postman_requests(items: list[dict]) -> list[dict]:
    requests: list[dict] = []
    for item in items:
        if "request" in item:
            requests.append(item["request"])
        requests.extend(postman_requests(item.get("item", [])))
    return requests


def main() -> None:
    files = [path for path in ROOT.rglob("*") if path.is_file() and ".git" not in path.parts]
    relative_files = {str(path.relative_to(ROOT)) for path in files}

    missing = REQUIRED_JSON - relative_files
    if missing:
        fail(f"missing required files: {', '.join(sorted(missing))}")

    for path in files:
        if path.name in FORBIDDEN_PATH_NAMES or path.suffix in {".key", ".pem"}:
            fail(f"forbidden credential file: {path.relative_to(ROOT)}")
        if path.suffix == ".json":
            json_file(str(path.relative_to(ROOT)))
        if path.suffix in {".png", ".ico"}:
            continue
        text = path.read_text(encoding="utf-8")
        for label, pattern in FORBIDDEN_PATTERNS.items():
            if pattern.search(text):
                fail(f"possible {label} in {path.relative_to(ROOT)}")

    server = json_file("server.json")
    if not isinstance(server, dict) or server.get("name") != "ai.draconic/market-intelligence":
        fail("server.json has the wrong registry name")
    if server.get("remotes") != [{"type": "streamable-http", "url": MCP_URL}]:
        fail("server.json has an unexpected remote endpoint")

    cursor = json_file("mcp.json")
    cursor_server = cursor.get("mcpServers", {}).get("draconic", {}) if isinstance(cursor, dict) else {}
    if cursor_server.get("url") != MCP_URL:
        fail("mcp.json has an unexpected remote endpoint")
    if cursor_server.get("auth", {}).get("scopes") != ["openid", "profile", "email", "offline_access"]:
        fail("mcp.json has unexpected OAuth scopes")

    cursor_plugin = json_file(".cursor-plugin/plugin.json")
    if cursor_plugin.get("repository") != "https://github.com/Betwizr/draconic-market-intelligence":
        fail("the Cursor plugin manifest has an unexpected repository URL")

    cline = json_file("configs/cline.mcp.json")
    cline_server = cline.get("mcpServers", {}).get("draconic", {}) if isinstance(cline, dict) else {}
    if cline_server.get("url") != MCP_URL or cline_server.get("type") != "streamableHttp":
        fail("the Cline configuration has the wrong endpoint or transport")
    if cline_server.get("autoApprove") != []:
        fail("the Cline configuration must not auto-approve tools")

    environment = json_file("postman/Draconic-Intelligence-API.postman_environment.json")
    values = environment.get("values", []) if isinstance(environment, dict) else []
    api_key = next((item for item in values if item.get("key") == "api_key"), None)
    if api_key is None or api_key.get("value") != "" or api_key.get("type") != "secret":
        fail("the Postman environment must contain an empty secret api_key value")

    collection = json_file("postman/Draconic-Intelligence-API.postman_collection.json")
    variables = collection.get("variable", []) if isinstance(collection, dict) else []
    base_url = next((item.get("value") for item in variables if item.get("key") == "base_url"), None)
    if base_url != API_URL:
        fail("the Postman collection has an unexpected production base URL")
    api_key_auth = collection.get("auth", {}).get("apikey", []) if isinstance(collection, dict) else []
    auth_values = {item.get("key"): item.get("value") for item in api_key_auth}
    if auth_values != {"key": "X-API-Key", "value": "{{api_key}}", "in": "header"}:
        fail("the Postman collection has unexpected API key authentication")
    requests = postman_requests(collection.get("item", []))
    paths = {request.get("url", {}).get("raw", "").removeprefix("{{base_url}}") for request in requests}
    if paths != EXPECTED_POSTMAN_PATHS:
        fail("the Postman collection request set changed unexpectedly")

    openapi = (ROOT / "postman/Draconic-Intelligence-API.openapi.yaml").read_text(encoding="utf-8")
    for path in {item.split("?")[0].replace("{{symbol}}", "{symbol}") for item in EXPECTED_POSTMAN_PATHS}:
        if f"  {path}:" not in openapi:
            fail(f"the OpenAPI contract is missing {path}")
    if "Cinder" in openapi:
        fail("the public OpenAPI contract contains an internal product codename")

    if json_file("submissions/docker/draconic/tools.json") != []:
        fail("Docker tools.json must be empty because tools are discovered dynamically")
    docker_yaml = (ROOT / "submissions/docker/draconic/server.yaml").read_text(encoding="utf-8")
    for required_line in (
        "type: remote",
        "category: finance",
        "transport_type: streamable-http",
        f"url: {MCP_URL}",
        "secret: draconic.personal_access_token",
    ):
        if required_line not in docker_yaml:
            fail(f"the Docker manifest is missing {required_line}")

    check_png("assets/logo-400.png", (400, 400))
    print(f"PASS: {len(files)} files parsed; endpoints, manifests, logo, and credential scan are clean.")


if __name__ == "__main__":
    main()
