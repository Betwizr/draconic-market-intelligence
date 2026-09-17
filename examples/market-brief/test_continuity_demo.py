"""Offline checks only. No network requests or credits are used."""
import json
from pathlib import Path
import tempfile
import urllib.error
import urllib.request
from unittest.mock import patch
from continuity_demo import NoRedirect, run, save_state

response = {'chat_id': 'example-conversation', 'analysis': 'A complete example answer.',
            'coverage': {'source_updated_at': '2026-09-17T09:45:00+00:00'}, 'chart': None}
with tempfile.TemporaryDirectory() as directory:
    state = Path(directory) / 'conversation.json'
    second = {**response, 'analysis': 'A distinct follow-up answer.', 'chart': {'type': 'example'}}
    with patch('continuity_demo.request', side_effect=[response, second]) as request:
        assert run('first', state, 'test-key') == response
        assert 'chat_id' not in request.call_args.args[0]
        assert run('update', state, 'test-key') == second
        assert request.call_args.args[0]['chat_id'] == 'example-conversation'
        assert request.call_count == 2
        assert 'test-key' not in state.read_text()
        assert len(json.loads(state.read_text())['responses']) == 2
        assert [r['response'] for r in json.loads(state.read_text())['responses']] == [response, second]
        try:
            run('first', state, 'test-key')
            raise AssertionError('An existing conversation was replaced')
        except FileExistsError:
            assert request.call_count == 2
    with patch('continuity_demo.request', side_effect=TimeoutError('Timed out')) as request:
        try:
            run('update', state, 'test-key')
            raise AssertionError('The timeout was not surfaced')
        except TimeoutError:
            assert json.loads(state.read_text())['request_pending']
        try:
            run('update', state, 'test-key')
            raise AssertionError('An unresolved request was duplicated')
        except ValueError:
            assert request.call_count == 1
    before = state.read_bytes()
    with patch('continuity_demo.os.replace', side_effect=OSError('Simulated disk failure')):
        try:
            save_state(state, {'replacement': True})
            raise AssertionError('Simulated write failure was hidden')
        except OSError:
            assert state.read_bytes() == before
    assert list(Path(directory).iterdir()) == [state]
try:
    NoRedirect().redirect_request(urllib.request.Request('https://api.draconic.ai/v1/agents/ask', headers={'X-API-Key': 'test-key'}), None, 302, 'Found', {}, 'https://different.example/')
    raise AssertionError('Redirect accepted')
except urllib.error.HTTPError as error:
    assert error.code == 302
print('PASS: one call per command, same conversation on update, optional chart, no stored key, existing-state protection, no retry after timeout.')
