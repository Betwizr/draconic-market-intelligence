"""Two explicit Draconic API requests with a conversation file you control."""
import argparse
import json
import os
from pathlib import Path
import tempfile
import urllib.error
import urllib.request

API_URL = 'https://api.draconic.ai/v1/agents/ask'
FIRST_QUESTION = (
    'Give a concise multi-timeframe read of NIFTY50 using the current or last-available data. '
    'Explain where the timeframes agree or conflict, the strongest supporting evidence, and the main uncertainty. '
    'State the actual source time. If the market is closed, describe this as a last-available snapshot. Analysis only.'
)
UPDATE_QUESTION = (
    'Challenge your previous NIFTY50 read. Identify the strongest conflicting evidence and explain whether it '
    'weakens your conclusion or only limits confidence. Name the observable evidence that would change the read. '
    'Use current or last-available data and state its source time. Do not imply the market moved merely because '
    'this is a follow-up; if the source snapshot is unchanged, say so. Analysis only.'
)


class NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        raise urllib.error.HTTPError(req.full_url, code, 'Redirect refused; API key was not forwarded', headers, fp)


def save_state(path, state):
    temporary = None
    try:
        with tempfile.NamedTemporaryFile(mode='w', dir=path.parent, prefix=path.name + '.', delete=False) as file:
            temporary = Path(file.name)
            json.dump(state, file, indent=2)
            file.flush()
            os.fsync(file.fileno())
        os.replace(temporary, path)
    finally:
        if temporary is not None and temporary.exists():
            temporary.unlink()


def request(body, api_key):
    message = urllib.request.Request(API_URL, data=json.dumps(body).encode(), headers={
        'Content-Type': 'application/json', 'Accept': 'application/json', 'X-API-Key': api_key})
    with urllib.request.build_opener(NoRedirect()).open(message, timeout=240) as response:
        return json.load(response)


def run(mode, state_path, api_key):
    state_path = Path(state_path)
    if mode == 'first':
        body = {'market': 'nse', 'instruments': ['NIFTY50'], 'timeframe': 'multi-timeframe', 'question': FIRST_QUESTION}
        state = {'request_pending': True, 'next_request': body, 'responses': []}
        # Exclusive creation prevents accidentally replacing another conversation.
        with state_path.open('x') as file:
            os.chmod(state_path, 0o600)
            json.dump(state, file, indent=2)
    else:
        state = json.loads(state_path.read_text())
        if state.get('request_pending') or not state.get('chat_id'):
            raise ValueError('The previous request is unresolved. Check its result before sending another request.')
        body = dict(state['last_request'], question=UPDATE_QUESTION, chat_id=state['chat_id'])
        state.update(request_pending=True, next_request=body)
        save_state(state_path, state)
    # One request only. A timeout leaves the pending marker in place; never retry automatically.
    response = request(body, api_key)
    if not response.get('analysis') or not response.get('chat_id') or not response.get('coverage', {}).get('source_updated_at'):
        raise ValueError('The response is incomplete. Inspect the request before retrying.')
    if mode == 'update' and response['chat_id'] != body['chat_id']:
        raise ValueError('The response did not continue the saved conversation.')
    history = state.get('responses', [])
    if not history and state.get('last_response'):
        history = [{'request': state['last_request'], 'response': state['last_response']}]
    history.append({'request': body, 'response': response})
    state = {'chat_id': response['chat_id'], 'request_pending': False, 'last_request': body,
             'last_response': response, 'responses': history}
    save_state(state_path, state)
    return response


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('mode', choices=['first', 'update'])
    parser.add_argument('--state', type=Path, required=True, help='Your local conversation file; use the same path for update.')
    args = parser.parse_args()
    key = os.environ.get('DRACONIC_API_KEY')
    if not key:
        parser.error('Set DRACONIC_API_KEY to your own key before running this example.')
    try:
        result = run(args.mode, args.state, key)
    except urllib.error.HTTPError as error:
        raise SystemExit(f'Draconic returned HTTP {error.code}. No retry was made; inspect the saved request before continuing.') from None
    except (OSError, ValueError) as error:
        raise SystemExit(f'{error} No retry was made.') from None
    print(result['analysis'])
    print('\nSource time:', result['coverage']['source_updated_at'])
    print('Conversation saved:', args.state)
