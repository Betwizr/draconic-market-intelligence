# Cline marketplace submission

The repository and issue copy are ready. Cline's official approval process requires one real test where Cline receives only the README (or an optional `llms-install.md`) and successfully connects. The README is sufficient here, so no extra installation file is needed.

## Issue title

```text
[Server Submission]: Draconic Market Intelligence
```

## Issue body

```markdown
## GitHub repository

https://github.com/Betwizr/draconic-market-intelligence

## Logo

https://raw.githubusercontent.com/Betwizr/draconic-market-intelligence/main/assets/logo-400.png

## Why add Draconic

Draconic brings current multi-signal market intelligence for supported instruments into the Cline workflow. Users can investigate an instrument, describe and evaluate an existing position, compare instruments or timeframes, challenge a thesis, and explore scenarios without leaving Cline.

The hosted remote server uses Streamable HTTP and OAuth. It exposes three focused tools: one open-ended analysis tool, one live-coverage tool, and one account-usage tool. Draconic provides analysis only. It cannot access a broker, place trades, change orders, or alter account settings.

Draconic is already active in the official MCP Registry. The repository contains only public installation files and documentation. It contains no proprietary server source or credentials.

## Installation test

- [ ] I gave Cline only this repository's README and confirmed that it connected through OAuth.
- [ ] Cline discovered exactly `ask_draconic`, `get_coverage`, and `get_account_usage`.
- [ ] I kept automatic tool approval disabled during the test.
```

Do not check the three installation boxes until the real Cline host test passes.

## Final gate

- [x] Public GitHub repository
- [x] 400x400 PNG logo
- [x] Hosted Streamable HTTP and OAuth setup documented in the README
- [x] Repository validator and clean tracked-file-copy validation pass
- [ ] Run one real Cline host test from the README alone
- [ ] Confirm OAuth completes and exactly three tools appear
- [ ] Create the submission issue at https://github.com/cline/mcp-marketplace/issues/new

The real Cline test is the only technical blocker. Creating the issue is an external publication and needs confirmation at the final submit action.
