# Long-tail directory submissions

Prepared on 2026-09-04. These are discovery listings, not separate product deployments.

## Execution order

1. **Awesome MCP Servers pull request** — one accepted PR also feeds Glama's synced directory.
2. **mcpservers.org** — direct free submission with a Finance category.
3. **MCP Market** — use its free queue first; the paid option only changes review speed and placement.
4. **Glama direct Add Server** — do not use this route for Draconic. Its public flow is for deploying a Dockerfile, while Draconic is already a hosted OAuth server. Use the Awesome-list sync instead.

Each form submission or pull request is public external communication and needs confirmation at the final submit action.

## Awesome MCP Servers -> Glama

- **Repository:** https://github.com/punkpeye/awesome-mcp-servers
- **Section:** `Finance & Fintech`
- **PR title:** `Add Draconic Market Intelligence 🤖🤖🤖`
- **Line to add:**

```markdown
- [Betwizr/draconic-market-intelligence](https://github.com/Betwizr/draconic-market-intelligence) 🎖️ ☁️ - Hosted, OAuth-protected market-intelligence MCP for supported Indian and global instruments. Three read-only tools provide open-ended analysis, current coverage, and shared account usage. Analysis only: no broker access or trade execution. Remote: `https://mcp.draconic.ai/mcp`; official registry: `ai.draconic/market-intelligence`.
```

- **PR body:**

```markdown
Adds Draconic Market Intelligence to Finance & Fintech.

The public integration repository documents a production hosted Streamable HTTP server, OAuth setup, three read-only tools, supported clients, and the official MCP Registry entry. Its validator parses every public configuration and scans tracked files for common secrets and private endpoints.
```

Before opening the PR, fork the list, insert the line in the Finance & Fintech section, and run the repository's normal formatting checks if any. Glama states that its web directory is synced from this repository, so do not create a separate container deployment.

## mcpservers.org

Submit at https://mcpservers.org/submit with:

- **Server Name:** Draconic Market Intelligence
- **Short Description:** Current multi-signal market intelligence for supported instruments through a hosted, OAuth-protected MCP server.
- **Link:** https://github.com/Betwizr/draconic-market-intelligence
- **Category:** Finance
- **Contact Email:** support@draconic.ai
- **Premium Submit:** Off. Start with the free listing.

## MCP Market

Submit at https://mcpmarket.com/submit with:

- **Type:** MCP Server
- **Source:** GitHub repo
- **GitHub repository:** https://github.com/Betwizr/draconic-market-intelligence
- **Notification email:** support@draconic.ai
- **Publication choice:** Free Queue

The paid `$29` option promises faster listing and a Try Now link. It is not required to validate discovery, so defer it until the free listing's referral traffic can be compared with other sources.

## Source requirements checked

- Cursor plugin reference and submission checklist: https://prod.cursor.com/docs/reference/plugins
- Cursor remote MCP and static OAuth configuration: https://prod.cursor.com/docs/mcp
- Cline official marketplace process: https://github.com/cline/mcp-marketplace
- Awesome MCP Servers contribution guide: https://github.com/punkpeye/awesome-mcp-servers/blob/main/CONTRIBUTING.md
- Glama directory sync statement: https://github.com/punkpeye/awesome-mcp-servers
- mcpservers.org form: https://mcpservers.org/submit
- MCP Market form: https://mcpmarket.com/submit
