---
name: clean-labels
description: Audit or adopt Clean Labels on GitHub repositories and choose or assign labels to issues and pull requests. Use for Clean Labels requests or adopting repositories; preserve existing conventions and distinguish label setup from item labeling.
---

# Clean Labels

Keep repository labels consistent and scannable. This skill works without
Clean Workflow or any other skill. Use GitHub Labels Template (GHLT) for
template setup and migration, and GitHub CLI or an available GitHub integration
for assigning existing labels to issues and PRs.

## Select the operation and repository

Establish the exact `owner/repo`, requested operation, and any issue or PR
number. Read repository instructions and fetch current labels and relevant
items. Paginate inventories before claiming completeness. Preserve an external
project's existing conventions unless adoption is explicitly in scope.

An audit or proposal is read-only. Labeling an item does not authorize creating
labels or replacing the repository's template. Additive setup does not
authorize deleting labels. Use existing authorization without asking again;
resolve only missing decisions that change the target or destructive scope.

## Convention

Names are lowercase, space-separated, and have no emoji prefix. Descriptions
use `[Category] Description [scope]` with sentence-style wording and no final
period. Scope is `[issues]`, `[PRs]`, or `[issues, PRs]`. API colors use six hex
characters without `#`.

| Name | Color | Description |
| --- | --- | --- |
| `bug` | `d73a4a` | [Type] Something isn't working [issues, PRs] |
| `enhancement` | `1a7f37` | [Type] New feature or improvement to existing functionality [issues, PRs] |
| `documentation` | `0075ca` | [Type] Improvements or additions to docs, README, or guides [issues, PRs] |
| `refactor` | `8957e5` | [Type] Code improvement without changing functionality [PRs] |
| `performance` | `e3795c` | [Type] Optimization, speed, or resource usage improvements [issues, PRs] |
| `security` | `d4a72c` | [Type] Security vulnerability or hardening [issues, PRs] |
| `blocked` | `cf222e` | [Status] Waiting on another issue, decision, or external factor [issues] |
| `needs triage` | `e16f24` | [Status] New issue — needs review and categorization [issues] |
| `awaiting response` | `1a7ec7` | [Status] Waiting for more information from the reporter [issues] |
| `ready` | `2da44e` | [Status] Triaged and ready to be picked up [issues] |
| `good first issue` | `7057ff` | [Community] Good for newcomers — well-scoped and documented [issues] |
| `help wanted` | `0e8a16` | [Community] Open for community contribution [issues] |
| `maintainer only` | `b60205` | [Community] Reserved for maintainers — not open for external contribution [issues, PRs] |
| `duplicate` | `cfd3d7` | [Resolution] This issue or pull request already exists [issues, PRs] |
| `invalid` | `cfd3d7` | [Resolution] This doesn't seem right [issues, PRs] |
| `wontfix` | `cfd3d7` | [Resolution] This will not be worked on [issues] |
| `core` | `0052cc` | [Area] Core logic, business rules, and primary functionality [issues, PRs] |
| `interface` | `5319e7` | [Area] User-facing layer — UI, CLI, API endpoints, or SDK surface [issues, PRs] |
| `data` | `006b75` | [Area] Database, storage, caching, or data models [issues, PRs] |
| `infra` | `e16f24` | [Area] Build system, CI/CD, deployment, config, and DevOps [issues, PRs] |
| `testing` | `1a7f37` | [Area] Unit tests, integration tests, E2E, and test tooling [issues, PRs] |

Choose exactly one Type, at most one Status, Community, and Resolution, and
any relevant Areas. Status applies to open issues, not PRs. Resolution explains
closure without completion and replaces Status; do not pair them. Assigning a
Resolution label alone is not permission to close the item. Follow scope tags;
the specification permits `refactor` on issues when the project tracks
refactoring work that way. Extra project labels can coexist with the core set;
event labels such as Hacktoberfest are optional, not part of the 21 core labels.

## Audit or set up the template

Check `ghlt --version` and `gh auth status` before using GHLT. If GHLT is
unavailable and installation is in scope, use the official
`github-labels-template` package; otherwise report the dependency and continue
with available read-only inspection. Do not expose authentication tokens.

Use explicit targeting in every command:

```sh
ghlt list --repo owner/repo
ghlt apply --repo owner/repo --exclude hacktoberfest,hacktoberfest-accepted
```

`list` inspects current definitions. `apply` adds missing template labels and
preserves existing definitions by default; use `--force` only when overwriting
matching names' template values is intended and authorized. Re-read the result
and report skipped mismatched definitions rather than claiming full conformity.
The exclusions keep GHLT v0.9.3's two optional event labels out of normal
setup. Omit them only when the user requests those event labels. Existing
event labels are preserved. Inspect the installed tool's help and template
before applying; adjust supported filters if a later version adds other
non-core labels.

For an explicitly authorized clean-slate migration, inspect `ghlt migrate
--help` and the template first. GHLT v0.9.3 migration has no exclusion option
and installs all 23 labels. If only the 21 core labels are requested, report
that limitation before any deletion and offer the filtered additive setup
above; do not run migration or pass it an unsupported `--exclude` flag.
Use `ghlt migrate -y --repo owner/repo` only when both deletion and the full
template, including event labels, are authorized. Migration can remove issue/PR
assignments; a request to adopt the convention alone does not authorize that
loss. Do not reproduce GHLT with custom scripts or individual API calls for
bulk template setup.

## Assign labels to an issue or PR

Read the item and its current labels, then choose from labels already present
in the target repository. For example, a new feature issue can use
`enhancement`, `needs triage`, and `interface`; a PR must omit `needs triage`.
If a needed label is absent, propose setup separately instead of creating it
as an incidental part of labeling the item.

Use GitHub CLI or a supported connector to apply the authorized additions and
remove superseded category labels as needed. Preserve unrelated custom labels.
When advancing an issue from `blocked` to `ready`, replace the old Status
rather than leaving both. Do not use a whole-label-list replacement that drops
other labels unless that exact result is intended.

## Verify and report

After template changes, list labels again. After item changes, fetch the item
again and verify its persisted labels. Compare the result with the intended
change and convention scope. For exhaustive audits or template verification,
use paginated GitHub API or connector reads when GHLT's inventory is limited;
do not treat an empty tool result as proof that no labels exist without a
successful authoritative read. Partial access, missing authentication, command
failure, or an uncertain write is not success. Re-fetch before retrying and
never blindly repeat a destructive migration after a partial failure.

## Source and maintenance

Derived from [Clean Labels specification v1.0.0](https://github.com/wgtechlabs/clean-labels/blob/main/SPECIFICATION.md)
and the [official GHLT implementation](https://github.com/warengonzaga/github-labels-template).
The core definitions are bundled here for independent installed use. This
repository owns the skill; keep it aligned with specification changes. Clean
Workflow can consume released copies downstream.
