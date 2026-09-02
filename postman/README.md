# Draconic Intelligence API for Postman

Import the collection and environment template into Postman. Create a revocable API key under Draconic Profile, then Agent & API Access, and place it only in the local `api_key` environment value.

The template contains no credential. Do not commit or publish an exported environment after adding a real key.

The collection separates the two behaviors:

- `Ask Draconic` and `Get Account Usage` require an API key.
- Coverage checks are public, free, and return no market prices.

The analysis endpoint is intended for meaningful supervisory calls from software. It is not a raw feed, per-tick signal, or execution service.
