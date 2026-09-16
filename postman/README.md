# Draconic Intelligence API for Postman

Import the collection and environment template into Postman. Create a revocable API key under Draconic Profile, then Agent & API Access, and place it only in the local `api_key` environment value.

The template contains no credential. Do not commit or publish an exported environment after adding a real key.

The collection includes named-instrument analysis and an explicit market-wide example for NSE/India or US. Running both analysis examples uses two credits. Options and news context depend on available data; no broker actions or alerts are performed. Pass the returned chat_id to continue an analysis rather than starting an unrelated conversation.

The collection separates the two behaviors:

- `Ask Draconic` and `Get Account Usage` require an API key.
- Coverage checks are public, free, and return no market prices.

The analysis endpoint is intended for meaningful supervisory calls from software. It is not a raw feed, per-tick signal, or execution service.

## Choose a workflow and handle the result

Read the [API workflow guide](https://draconic.ai/api#api-guide) for six practical scenarios, request examples, and current integration limits.

For related updates, copy the returned `chat_id` into the next request body. The service uses up to twenty recent turns; retain complete responses in your own system for longer comparisons. Each successful analysis uses one credit.

The response is JSON, but `analysis` is Markdown text. Ask a market question, not for code or a new output schema. Keep the complete analysis, source timing, contrary evidence, and “What changes the read”. If another model extracts fields or summarizes it, validate that output and preserve the original. Missing values are unknown, not zero.

Send one intelligence request at a time per account. Correct authentication, credit, coverage, or request errors before retrying. After a timeout, check usage and history before repeating a request: the original can still have completed and consumed a credit. No idempotency guarantee is provided. Never publish a real key in a shared environment or collection.
