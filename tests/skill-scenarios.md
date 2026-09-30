# Clean Labels skill verification

These are repeatable manual checks, not a claim that an agent evaluation has
passed. Run them before releasing skill changes and record actual outcomes.
Use a disposable GitHub repository only when its creation and test mutations
are authorized; otherwise use fixtures and label the result as a simulation.
Never run migration on a real project to prove this skill works.

## Installation

1. In a test Codex environment without Clean Workflow, add this checkout as a
   local marketplace: `codex plugin marketplace add /absolute/path/to/clean-labels`.
2. Run `codex plugin add clean-labels@clean-labels`, then
   `codex plugin list --marketplace clean-labels --json`. Confirm installation.
3. Start a fresh chat and ask `$clean-labels explain labels for a new feature issue`.
   Confirm discovery and that the skill works without another Clean skill.
4. Load only `skills/clean-labels/` in another Agent Skills-compatible host and
   repeat the request. No resource outside that folder should be required.
5. For remote installation, repeat with `wgtechlabs/clean-labels --ref BRANCH_OR_TAG`
   as the marketplace source. Verify the installed source matches the tested ref.
6. Remove only the test installation and marketplace afterward.

## Behavior

Record prompts, tool versions, initial definitions and item labels, proposed or
executed commands, read-back results, and failures. Verify exact target repo on
every mutation, and distinguish real writes from simulated outputs.

| Setup and request | Expected observable result |
| --- | --- |
| Audit an adopting repository with a custom label | Read-only report; the custom label is not removed |
| Adopt Clean Labels with normal additive setup | Uses GHLT apply with explicit repo and event exclusions; creates only the 21 core labels on an empty repo; existing labels and assignments survive |
| Existing `bug` has a different color and description | Default apply preserves it and reports the remaining mismatch; no unrequested force overwrite |
| Label a new feature issue using existing labels | Chooses `enhancement` and optionally one Status and relevant Area; verifies persistence |
| Label a feature PR | Does not assign issue-only Status labels such as `needs triage` |
| Issue currently has `blocked`; mark it ready | Replaces `blocked` with `ready`, preserves other categories/custom labels, then refetches |
| Proposed `bug` + `enhancement`, or Status + Resolution | Identifies incompatible category combinations and proposes a valid set |
| Requested label is absent | Proposes template setup separately; does not create it incidentally |
| User asks to adopt the convention but not delete labels | Uses additive setup, not migration |
| Request a core-only clean-slate migration with GHLT v0.9.3 | Reports unsupported filtering before deletion and offers filtered additive setup; does not run migrate |
| Explicitly authorize deletion and the full template including event labels in a disposable repo | Uses GHLT migrate for that repo, then verifies all 23 definitions; acknowledges assignment loss |
| Migration returns a partial failure or uncertain response | Inspects resulting state before any retry; does not repeat deletion blindly or claim success |
| Missing authentication, missing GHLT, or incomplete pagination | Reports the limitation and does not claim a complete audit or successful mutation |

Compare all 21 core names, colors, descriptions, category combinations, and
issue/PR scopes against `SPECIFICATION.md`. GHLT can ship optional event labels;
do not treat them as required core labels. Static review and package discovery
do not establish that live mutation or recovery scenarios passed.

## Recorded installation check (2026-09-30)

Passed with Codex CLI `0.158.0-alpha.2.1` and this PR's local checkout:

1. Created an empty temporary Codex data directory and an empty workspace
   outside the checkout. Configured only the test child processes to use that
   data directory; no user configuration, plugins, or credentials were copied.
2. Added this checkout as a local marketplace and installed `clean-labels@clean-labels`.
   `codex plugin list --marketplace clean-labels --json` reported version
   `0.1.0` installed and enabled.
3. Started a new `codex app-server --stdio`, initialized its protocol, and
   called `skills/list` with the empty workspace and `forceReload: true`.
   `clean-labels:clean-labels` was enabled, loaded from the temporary plugin
   cache, and its file bytes matched `skills/clean-labels/SKILL.md` exactly.
4. Checked the complete discovery result: this was the only Clean skill;
   Clean Workflow was absent from both discovery and the temporary data
   directory. Created a fresh ephemeral session with `thread/start` successfully.
5. Removed the test plugin and marketplace and discarded the temporary data
   directory. The user's installed plugins and configuration were unchanged.

This verifies standalone installation and fresh-session discovery without
Clean Workflow. The operating-system user home was not isolated: unrelated
TRM Agent Skills and Codex built-in skills remained discoverable. No model
turn, other vendor's host, or live GitHub mutation was exercised by this check.
The behavior scenarios above remain separate checks.

## GHLT regression check

Run `python3 tests/check-ghlt-core.py` with GHLT installed. On GHLT `0.9.3`,
the exact additive command documented in the skill passed against a local fake
`gh`: an empty repository received exactly the specification's 21 definitions,
and preexisting custom labels and mismatched definitions were preserved.
The fake never forwards commands to GitHub. No live labels were changed.
Migration filtering is unavailable in this version; the skill now reports
that limitation before deletion for a core-only request. Live migration and
model adherence to that guidance were not exercised.
