# Ask for a market read, then challenge it in the same conversation

This Python example makes one Draconic analysis request when you run `first`. When you choose to run `update`, it sends a follow-up using the conversation identifier returned by the first request. Each successful analysis uses one credit from your Draconic account. The script does not poll or retry automatically.

The first question asks for a multi-timeframe view of NIFTY50. The follow-up asks Draconic to challenge that view using conflicting evidence. You can run the follow-up immediately or later. An immediate follow-up may use the same market snapshot, so the example explicitly asks Draconic not to imply that prices moved just because another question was asked.

## Run the two requests when you choose

Use Python 3.9 or newer. No packages need to be installed. Set `DRACONIC_API_KEY` in your environment to your own Draconic key. Keep the key out of the script and the conversation file.

Run the first request with a new file path:

```sh
python3 continuity_demo.py first --state ./nifty-conversation.json
```

Read the answer, then run the follow-up using the same file:

```sh
python3 continuity_demo.py update --state ./nifty-conversation.json
```

The file belongs to you. It contains the conversation identifier and the complete requests and responses, including source times and optional chart data. The script prints the latest analysis and source time. It does not render charts. Keep this file private if your questions contain private information. Run one command at a time against a state file; this is a local example, not a concurrent job scheduler.

The two questions are ordinary strings near the top of `continuity_demo.py`; replace them with your own questions if useful. The first request omits `chat_id`. The follow-up includes the saved `chat_id`, which tells Draconic to use the same conversation. The API remains analysis-only and does not place trades.

## Understand an uncertain result before trying again

A request can time out after the server has started work. The script records that a request is pending before sending it and refuses another command until that result has been resolved. Check your conversation and credit history before deciding whether to repeat the request. Do not clear the pending marker merely to retry an uncertain paid request.

To begin an unrelated conversation, choose a different state-file path. The `first` command refuses to replace an existing file. The API key must belong to the same account when continuing a saved conversation.

## Check the example without making paid requests

```sh
python3 test_continuity_demo.py
```

The offline check verifies conversation reuse, preservation of complete responses, optional charts, refusal to forward your key through redirects, safe state replacement and no retry after an uncertain result. A live two-request test on 17 September 2026 returned the same conversation identifier and used two credits. This verifies the integration pattern, not every market interpretation in a generated answer. Different price and options sources can have different timestamps; preserve the timing inside the answer as well as the response-level source time.
