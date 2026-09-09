# Draconic Market Intelligence

Bring Draconic's current multi-signal market intelligence into the artificial-intelligence workflow you already use.

Draconic is a hosted Model Context Protocol service. Model Context Protocol, or MCP, is the standard that lets an artificial-intelligence client call an external tool. Nothing runs on your computer, and this repository contains no proprietary Draconic server code.

The live endpoint is:

```text
https://mcp.draconic.ai/mcp
```

The server is also active in the [official MCP Registry](https://registry.modelcontextprotocol.io/v0.1/servers?search=ai.draconic%2Fmarket-intelligence).

[![Listed on mcpservers.org](https://mcpservers.org/badge.svg)](https://mcpservers.org/servers/betwizr/draconic-market-intelligence)

## Connect Draconic

Every client opens the Draconic sign-in and consent screen. The connection uses your existing Draconic account and shared credit balance.

### Claude Code

```bash
claude mcp add --scope user --transport http draconic https://mcp.draconic.ai/mcp
```

### Codex

```bash
codex mcp add draconic --url https://mcp.draconic.ai/mcp
codex mcp login draconic --scopes openid,profile,email,offline_access
```

Complete the browser sign-in, then restart your Codex session. Adding the server alone does not sign you in. Ask Codex to check your Draconic account usage first; that check is free.

The native MCP connection above is separate from using the installed ChatGPT plugin inside Codex. On September 9, the plugin path returned an analysis-response error even though Draconic generated the answer. That client-specific issue remains under investigation; do not repeatedly retry a charged analysis. Account-usage checks still work.

### Cursor

Install the plugin after its marketplace listing is approved. For manual setup, copy the `draconic` entry from [`mcp.json`](mcp.json) into your Cursor MCP configuration.

### Cline

Open **MCP Servers**, choose **Remote Servers**, and use these values:

- Set the server name to `draconic`.
- Set the server URL to `https://mcp.draconic.ai/mcp`.
- Choose **Streamable HTTP** as the transport.
- Keep automatic tool approval disabled.

The equivalent configuration is available in [`configs/cline.mcp.json`](configs/cline.mcp.json).

### Docker MCP Toolkit

The Docker catalog submission is prepared but is not live yet. Once Docker approves it, add Draconic from the MCP Toolkit catalog and complete the browser sign-in. Draconic is a hosted remote server, so no Draconic container or Docker image is required.

### Other MCP clients

Add `https://mcp.draconic.ai/mcp` as a remote Streamable HTTP server. Complete the browser sign-in when the client asks you to authorize Draconic. Clients that do not support remote Streamable HTTP servers and OAuth cannot connect directly.

## What the tools do

- `ask_draconic` answers an open-ended analytical question about one to five currently supported instruments. It also accepts `market_wide=true` for supported market and sector context without inventing an anchor instrument. A successful answer uses one existing Draconic credit.
- `get_coverage` reports the currently supported markets, instruments, and timeframes. It is free and returns no market prices.
- `get_account_usage` reports the authenticated account's shared Draconic credit balance. It is free.

Use `get_coverage` for the current instrument universe. Coverage changes as data sources are activated or paused, so this repository does not freeze a symbol count.

Draconic provides analysis only. These tools cannot access a broker, place a trade, change an order, create an alert, or change account settings.

## What has been verified

- Claude Code and native Codex MCP have completed real free and paid calls. Native Codex analysis and the one-credit charge were reverified on September 9, 2026. This does not claim chart rendering in every client.
- Cursor has completed OAuth sign-in and discovered all three tools.
- Cline and Docker installation files are prepared for host testing and marketplace review. They are not described as host-verified yet.

## Direct API

Software can call the same Draconic intelligence through the direct API. The Postman collection and safe environment template are in [`postman`](postman). Create a revocable key under **Draconic Profile**, then **Agent & API Access**. Never commit or publish that key.

The direct API is intended for meaningful supervisory calls from an algo, terminal, alerting system, research workflow, or software product. It is not a raw feed, per-tick signal, execution service, or high-frequency trading interface.

## Product and support

- [Product page and setup guide](https://draconic.ai/agents)
- [Privacy policy](https://draconic.ai/privacy-policy)
- [Terms of service](https://draconic.ai/terms-of-service)
- [Disclaimer](https://draconic.ai/disclaimer)
- For support, email support@draconic.ai. The [setup guide](https://draconic.ai/agents) explains account access and installation.

The MIT License covers the public documentation, configuration files, and validation script in this repository. It does not license the hosted Draconic service, its models, data, system prompts, or proprietary market-intelligence methods.

## Validate this repository

The validation uses only Python's standard library. It parses every JSON file, checks the exact public endpoints and manifests, checks the marketplace logo dimensions, and scans tracked content for common credential and private-endpoint patterns.

```bash
python3 scripts/validate.py
```
