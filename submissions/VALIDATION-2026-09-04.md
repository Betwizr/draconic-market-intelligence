# Marketplace validation evidence — 2026-09-04

## Confirmed

- GitHub reports `Betwizr/draconic-market-intelligence` as a public repository with `main` as its default branch.
- `python3 scripts/validate.py` passes on the working tree.
- A clean copy made from tracked repository files also passes the same validator.
- Every JSON file parses.
- The public MCP endpoint returns `401 Unauthorized` without credentials and advertises protected-resource metadata rather than exposing a tool call anonymously.
- `https://mcp.draconic.ai/.well-known/oauth-protected-resource/mcp` identifies the exact MCP resource, authorization server, bearer-header method, and the four requested scopes.
- The advertised authorization server exposes authorization, token, and dynamic-registration endpoints and supports authorization-code flow.
- Cursor's installed CLI is version `3.18.25`. A prior real Cursor host test completed OAuth and discovered the three expected tools.

## Commands

```bash
python3 scripts/validate.py
git diff --check

TEMP_COPY=$(mktemp -d /tmp/draconic-marketplace-XXXXXX)
git ls-files -z | tar --null -T - -cf - | tar -xf - -C "$TEMP_COPY"
python3 "$TEMP_COPY/scripts/validate.py"
rm -rf "$TEMP_COPY"

curl -D - https://mcp.draconic.ai/mcp
curl https://mcp.draconic.ai/.well-known/oauth-protected-resource/mcp
```

## Still unverified

- The current Cline host has not been given only this README and taken through a real OAuth connection. Do this before checking the test boxes in the Cline issue.
- The Cursor marketplace has not parsed the final public commit yet. Push the manifest cleanup before entering the repository URL in its publisher form.
- No directory form, issue, or pull request in this folder has been submitted. Those are public external actions and remain final-confirmation gates.
