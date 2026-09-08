# Draconic Intelligence API for Postman

Import the collection and environment template into Postman. Create a revocable API key under Draconic Profile, then Agent & API Access, and place it only in the local `api_key` environment value.

The template contains no credential. Do not commit or publish an exported environment after adding a real key.

The collection includes named-instrument analysis and an explicit market-wide example for NSE/India or US. Running both analysis examples uses two credits. Options and news context depend on available data; no broker actions or alerts are performed. Pass the returned chat_id to continue an analysis rather than starting an unrelated conversation.

The collection separates the two behaviors:

- `Ask Draconic` and `Get Account Usage` require an API key.
- Coverage checks are public, free, and return no market prices.

The analysis endpoint is intended for meaningful supervisory calls from software. It is not a raw feed, per-tick signal, or execution service.
