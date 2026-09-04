# Cursor marketplace submission

## Submission fields

- **Repository:** https://github.com/Betwizr/draconic-market-intelligence
- **Plugin name:** draconic-market-intelligence
- **Product name:** Draconic Market Intelligence
- **Description:** Bring Draconic's current multi-signal market intelligence into Cursor.
- **Homepage:** https://draconic.ai/agents
- **Publisher:** Six Singularities Private Limited
- **License:** MIT for this public integration repository

## Evidence and final gate

- [x] The GitHub repository is public on its `main` branch.
- [x] `.cursor-plugin/plugin.json`, `mcp.json`, README, and a repository-relative logo are present.
- [x] The manifest uses only documented Cursor plugin fields and the plugin name is lowercase kebab-case.
- [x] The static OAuth configuration follows Cursor's documented `auth.CLIENT_ID` and `auth.scopes` shape.
- [x] A real Cursor host test completed OAuth and discovered exactly `ask_draconic`, `get_coverage`, and `get_account_usage`.
- [x] A clean tracked-file copy passed `python3 scripts/validate.py`.
- [ ] Push the final manifest cleanup to public `main`.
- [ ] At https://cursor.com/marketplace/publish, enter the repository URL, review Cursor's publisher terms, and submit.

The last step is an external marketplace submission and terms acceptance, so it needs the account holder's confirmation at the submit button.
