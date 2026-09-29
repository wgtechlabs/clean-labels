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
| Adopt Clean Labels with normal additive setup | Uses GHLT apply with explicit repo; existing labels and assignments survive |
| Existing `bug` has a different color and description | Default apply preserves it and reports the remaining mismatch; no unrequested force overwrite |
| Label a new feature issue using existing labels | Chooses `enhancement` and optionally one Status and relevant Area; verifies persistence |
| Label a feature PR | Does not assign issue-only Status labels such as `needs triage` |
| Issue currently has `blocked`; mark it ready | Replaces `blocked` with `ready`, preserves other categories/custom labels, then refetches |
| Proposed `bug` + `enhancement`, or Status + Resolution | Identifies incompatible category combinations and proposes a valid set |
| Requested label is absent | Proposes template setup separately; does not create it incidentally |
| User asks to adopt the convention but not delete labels | Uses additive setup, not migration |
| Explicitly authorized clean-slate migration in a disposable repo | Uses GHLT migrate for that repo, then verifies definitions; acknowledges assignment loss |
| Migration returns a partial failure or uncertain response | Inspects resulting state before any retry; does not repeat deletion blindly or claim success |
| Missing authentication, missing GHLT, or incomplete pagination | Reports the limitation and does not claim a complete audit or successful mutation |

Compare all 21 core names, colors, descriptions, category combinations, and
issue/PR scopes against `SPECIFICATION.md`. GHLT can ship optional event labels;
do not treat them as required core labels. Static review and package discovery
do not establish that live mutation or recovery scenarios passed.
