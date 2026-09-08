# Postman public workspace publication pack

This pack defines the exact public metadata and the checks required before publication. It does not contain a credential.

## Workspace metadata

- **Workspace name:** Draconic Developers
- **Visibility:** Public
- **Publisher:** Six Singularities Private Limited
- **Workspace summary:** Official Draconic integrations for agents, trading systems, terminals, alerts, research workflows, and software products.
- **Workspace description:** Add Draconic's current multi-signal market intelligence to software at meaningful supervisory decision points. The workspace contains the official OpenAPI contract, a runnable Postman collection, and a credential-free environment template. Draconic provides analysis only. It is not a raw market-data feed or execution service.
- **Support:** support@draconic.ai
- **Product page:** https://draconic.ai/agents

## API metadata

- **API name:** Draconic Intelligence API
- **Version:** 1.0.0
- **Summary:** Add Draconic's analysis-only market intelligence to an algo, terminal, alerting system, research workflow, or software product.
- **Categories:** Finance, Artificial Intelligence, Developer Tools
- **Tags:** market-intelligence, trading, agents, analysis, fintech
- **Production base URL:** https://api.draconic.ai
- **Authentication:** Revocable `X-API-Key` created in Draconic Profile under Agent & API Access

## Publication checklist

September8 validation: the updated collection's exact five HTTP requests passed against production using a temporary in-memory key. Both analysis requests completed and the observed plan balance decreased by exactly two credits. Both coverage requests passed without authentication, account usage passed, and the key was revoked. This was a collection-request smoke harness, not a Postman UI or Newman run. The local collection/OpenAPI examples include market_wide; the hosted Postman copy still needs synchronization. No account responses or real keys are saved in this public pack.

- [x] Create the public `Draconic Developers` workspace under the clean company publisher account.
- [x] Import `Draconic-Intelligence-API.openapi.yaml` as API version 1.0.0.
- [x] Import `Draconic-Intelligence-API.postman_collection.json`.
- [x] Import `Draconic-Intelligence-API.postman_environment.json` and confirm that `api_key` is empty.
- [x] Run both coverage requests without authentication and confirm that they return no market prices.
- [ ] Put a temporary revocable Draconic API key only in the private local environment.
- [x] Run `Get Account Usage` and confirm that it does not consume a credit.
- [x] Run both analysis examples and confirm that the combined observed deduction is two credits.
- [ ] Remove the temporary key from the environment before publishing or exporting anything.
- [ ] Confirm that no saved example contains a user question, market response, token, account identifier, or credit balance from the test account.
- [x] Publish the API, collection, and credential-free environment.
- [x] Confirm through the Postman API that the workspace is public and contains the collection, environment, and OpenAPI specification.
- [ ] Add the final public Postman URL to https://draconic.ai/agents.
