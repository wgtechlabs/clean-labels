"""Exercise the documented setup using installed GHLT and a local fake gh.

Run: python3 tests/check-ghlt-core.py
Requires GHLT on PATH. Never calls GitHub or changes real labels.
"""
import json
import os
from pathlib import Path
import re
import shlex
import shutil
import subprocess
import sys
import tempfile

root = Path(__file__).resolve().parents[1]
ghlt = shutil.which('ghlt')
if not ghlt:
    raise SystemExit('Install github-labels-template before running this check')
commands = set()
for path in ('skills/clean-labels/SKILL.md', 'README.md', 'QUICK-REFERENCE.md'):
    examples = re.findall(r'^(?:ghlt|npx github-labels-template) (apply .+|apply)$',
                          (root / path).read_text(), re.MULTILINE)
    assert examples, path
    for example in examples:
        args = [ghlt, *shlex.split(example)]
        if '--repo' in args:
            args[args.index('--repo') + 1] = 'fixture/core'
        else:
            args.extend(['--repo', 'fixture/core'])
        commands.add(tuple(args))
expected = {
    name: {'color': color, 'description': description}
    for name, color, description in re.findall(
        r'^\| `([^`]+)` \| `([0-9a-f]{6})` \| `([^`]+)` \|$',
        (root / 'SPECIFICATION.md').read_text(), re.MULTILINE)
}
assert len(expected) == 21
with tempfile.TemporaryDirectory(prefix='ghlt-core-') as directory:
    work = Path(directory)
    state = work / 'labels.json'
    fake = work / 'gh'
    fake.write_text('#!' + sys.executable + '\n' + '''import json, sys
from pathlib import Path
a = sys.argv[1:]
p = Path(__file__).with_name('labels.json')
labels = json.loads(p.read_text())
if a == ['--version'] or a == ['auth', 'status']:
    pass
elif a[:2] == ['label', 'list'] and a[a.index('--repo')+1] == 'fixture/core':
    print('\\n'.join(labels))
elif a[:2] == ['label', 'create'] and a[a.index('--repo')+1] == 'fixture/core':
    assert a[2] not in labels, a
    labels[a[2]] = {'color': a[a.index('--color')+1],
                    'description': a[a.index('--description')+1]}
    p.write_text(json.dumps(labels))
else:
    raise SystemExit('Unexpected gh call: ' + repr(a))
''')
    fake.chmod(0o755)
    environment = dict(os.environ, PATH=str(work) + os.pathsep + os.environ['PATH'])
    for args in sorted(commands):
        selected = expected
        if '--category' in args:
            category = args[args.index('--category') + 1]
            selected = {name: label for name, label in expected.items()
                        if label['description'].lower().startswith('[' + category + ']')}
            assert selected, category
        for initial in ({}, {'custom': {'color': '123456', 'description': 'Keep me'},
                            'bug': {'color': '000000', 'description': 'Keep mismatch'}}):
            state.write_text(json.dumps(initial))
            result = subprocess.run(args, cwd=work, env=environment, text=True,
                                    capture_output=True, timeout=60)
            assert result.returncode == 0, result.stdout + result.stderr
            actual = json.loads(state.read_text())
            assert actual == {**selected, **initial}, (args, actual)
    print(f'PASS: {len(commands)} setup variants across skill, README, and quick reference; '
          'only core labels selected; existing definitions preserved')
