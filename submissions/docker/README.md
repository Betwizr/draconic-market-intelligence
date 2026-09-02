# Docker MCP Catalog submission

Copy the `draconic` directory into `servers/draconic` in a current fork of `docker/mcp-registry`.

Then run Docker's own checks:

```bash
task validate -- --name draconic
task catalog -- draconic
```

Import the generated catalog into Docker Desktop, authorize Draconic through OAuth, and confirm that the toolkit discovers exactly three tools. Open the pull request only after that host test passes.

This is a remote hosted server. Do not add a Dockerfile, image, local server package, API key, or hard-coded access token.
