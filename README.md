# Clean Labels

> **Clean Repos deserve Clean Labels.**

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Version](https://img.shields.io/badge/version-1.0.0-green.svg)](https://github.com/wgtechlabs/clean-labels)

A standardized GitHub label convention designed to be consistent, scannable, and universal. Clean Labels defines a curated set of labels organized into 5 clear categories — every label follows the same format so your team always knows what they're looking at.

**Note:** This is a documented convention refined through real-world open source practice. The [github-labels-template](https://github.com/warengonzaga/github-labels-template) CLI tool is the official implementation for applying Clean Labels to any repository.

---

## Install the agent skill

Install **Clean Labels** as a standalone skill for AI assistants. It includes its
own instructions and works without Clean Workflow or another Clean skill.
You can also use the convention manually with the guides below.

### Requirements

Use a Codex version with `codex plugin` support; installation and discovery
were verified with Codex CLI `0.158.0-alpha.2.1`.
Repository operations need authenticated GitHub access. Template setup uses the official [GitHub Labels Template (GHLT)](https://github.com/warengonzaga/github-labels-template) CLI; installing this skill does not install GHLT.

### Install in Codex

Install the stable version from `main`:

```sh
codex plugin marketplace add wgtechlabs/clean-labels --ref main
codex plugin add clean-labels@clean-labels
codex plugin list --marketplace clean-labels --json
```

Confirm the plugin is installed and enabled, then start a new chat and invoke
`$clean-labels`. Installation alone does not authorize repository changes.

### Example requests

```text
$clean-labels audit the labels in owner/repo without changing them

$clean-labels adopt the 21 core labels in owner/repo and preserve existing labels

$clean-labels label PR 42 in owner/repo using its existing labels
```

Audits are read-only. Additive setup preserves existing labels; destructive
migration needs explicit authorization. Normal setup excludes optional event
labels. With GHLT `0.9.3`, core-only migration is unsupported, so the skill
reports that limitation before deletion and offers additive setup.

### Other Agent Skills hosts

Load the entire [`skills/clean-labels/`](skills/clean-labels/SKILL.md) folder using
your host's skill installation mechanism. The instructions are self-contained;
the host must still provide the tools required for the requested operation.
Other vendors' hosts have not been verified in this repository's test record.

[Clean Workflow](https://github.com/wgtechlabs/clean-workflow) provides broader
development, review, and delivery guidance. Choose this standalone plugin for
Clean Labels alone. This repository owns the skill; updates to the broader bundle
are maintained separately.

### Update or remove

Refresh the configured marketplace and reinstall its plugin:

```sh
codex plugin marketplace upgrade clean-labels
codex plugin remove clean-labels@clean-labels
codex plugin add clean-labels@clean-labels
```

Start a new chat after updating. To uninstall and remove its marketplace:

```sh
codex plugin remove clean-labels@clean-labels
codex plugin marketplace remove clean-labels
```

### Preview development changes

To test `dev` before promotion to `main`, first remove an existing installation
and same-named marketplace with the commands above, then run:

```sh
codex plugin marketplace add wgtechlabs/clean-labels --ref dev
codex plugin add clean-labels@clean-labels
```

Use another branch or an existing tag instead of `dev` to test a specific ref.
For local development, use the absolute checkout path as the marketplace source
and omit `--ref`. Switch back to the stable installation commands after testing.
See [skill verification](tests/skill-scenarios.md) for recorded installation
results, behavior scenarios, and verification limits.

The current installable package version is tracked in
[`.codex-plugin/plugin.json`](.codex-plugin/plugin.json). The version badge at
the top of this README refers to the convention specification, not the plugin.

### Automated releases

Pushes to `main`, including a merged promotion PR, run the
[release workflow](.github/workflows/release.yml). It uses the same pinned
[Release Build Flow Action](https://github.com/wgtechlabs/release-build-flow-action)
configuration as Clean Coding and Clean Code Review: plan the version, update
the plugin manifest, then commit `CHANGELOG.md` and publish a tag and GitHub
Release when a version bump is needed. Existing release tags determine the
next version; `0.1.0` is the initial version when no tags exist. Other package
manifests are not synchronized by this workflow.

### Skill ownership

This repository is the canonical source for `clean-labels`. Maintain its skill
alongside [SPECIFICATION.md](SPECIFICATION.md), which remains authoritative.
Keep instructions self-contained and check examples against the specification.
Downstream bundles should import a released skill directory and record its
version and source commit, rather than maintain independent edits. A bundle
can lag until its update is reviewed and merged.

---

## Why Clean Labels?

Default GitHub labels are **inconsistent**. Across projects you see `bug`, `Bug`, `bug report`, `🐛 bug` — all meaning the same thing. Labels get bloated, duplicated, and abandoned.

Clean Labels is different:
- 🏷️ **Consistent**: Every label follows `[Category] Description [scope]` format
- 🎯 **Scannable**: 5 logical categories cover every workflow need
- 📐 **Opinionated**: 21 curated labels — no noise, no gaps
- 🚀 **Universal**: Works for any project type, size, or team

---

## The Convention Format

Every Clean Label description follows this structure:

```
[Category] Description [scope]
```

Where:
- `[Category]` — One of: `Type`, `Status`, `Community`, `Resolution`, `Area`
- `Description` — Plain English, sentence-style
- `[scope]` — Where it applies: `[issues]`, `[PRs]`, or `[issues, PRs]`

**Example:**
```
[Type] Something isn't working [issues, PRs]
```

---

## The 21 Labels

### 🔴 Type — Classify what kind of work this is

| Name | Color | Description |
|------|-------|-------------|
| `bug` | `#d73a4a` | Something isn't working |
| `enhancement` | `#1a7f37` | New feature or improvement to existing functionality |
| `documentation` | `#0075ca` | Improvements or additions to docs, README, or guides |
| `refactor` | `#8957e5` | Code improvement without changing functionality |
| `performance` | `#e3795c` | Optimization, speed, or resource usage improvements |
| `security` | `#d4a72c` | Security vulnerability or hardening |

### 🟡 Status — Track the current workflow state

| Name | Color | Description |
|------|-------|-------------|
| `blocked` | `#cf222e` | Waiting on another issue, decision, or external factor |
| `needs triage` | `#e16f24` | New issue — needs review and categorization |
| `awaiting response` | `#1a7ec7` | Waiting for more information from the reporter |
| `ready` | `#2da44e` | Triaged and ready to be picked up |

### 🟣 Community — Signals for open source contributors

| Name | Color | Description |
|------|-------|-------------|
| `good first issue` | `#7057ff` | Good for newcomers — well-scoped and documented |
| `help wanted` | `#0e8a16` | Open for community contribution |
| `maintainer only` | `#b60205` | Reserved for maintainers — not open for external contribution |

### ⚪ Resolution — Why an issue or PR was closed

| Name | Color | Description |
|------|-------|-------------|
| `duplicate` | `#cfd3d7` | This issue or pull request already exists |
| `invalid` | `#cfd3d7` | This doesn't seem right |
| `wontfix` | `#cfd3d7` | This will not be worked on |

### 🔵 Area — Broad software layers, universal across any project

| Name | Color | Description |
|------|-------|-------------|
| `core` | `#0052cc` | Core logic, business rules, and primary functionality |
| `interface` | `#5319e7` | User-facing layer — UI, CLI, API endpoints, or SDK surface |
| `data` | `#006b75` | Database, storage, caching, or data models |
| `infra` | `#e16f24` | Build system, CI/CD, deployment, config, and DevOps |
| `testing` | `#1a7f37` | Unit tests, integration tests, E2E, and test tooling |

---

## Quick Start

### Apply with CLI (Recommended)

Use the official [github-labels-template](https://github.com/warengonzaga/github-labels-template) CLI tool:

```bash
# Apply the 21 core labels to the current repo
npx github-labels-template apply --exclude hacktoberfest,hacktoberfest-accepted

# Apply labels from a specific category
npx github-labels-template apply --category type

# Apply to a specific repo
npx github-labels-template apply --repo owner/repo --exclude hacktoberfest,hacktoberfest-accepted
```

The exclusions omit GHLT's optional Hacktoberfest labels. Omit the exclusions
only when those event labels are wanted. Default `apply` adds missing labels
and preserves existing definitions, including mismatched colors or descriptions;
inspect the result before claiming full conformity. GHLT `0.9.3` migration
installs all 23 labels and has no exclusion option. Use filtered additive setup
for core-only adoption; do not run migration expecting it to keep only 21 labels.

### Apply Manually via GitHub API

```bash
# Example: create the "bug" label
gh label create "bug" --color "d73a4a" --description "[Type] Something isn't working [issues, PRs]"
```

---

## Category Design Principles

### Type — The "what"
Every issue or PR has a type. Types classify the nature of the work — not its workflow state. A bug is still a bug whether it's open, blocked, or resolved.

### Status — The "where in the process"
Status labels reflect the current state of an item in your workflow. They answer "where is this right now?" — not what it is or who it's for.

### Community — The "who"
Community labels signal contributor-facing intent. They answer "who should work on this?" — helping maintainers and contributors quickly find appropriate work.

### Resolution — The "why it closed"
Resolution labels explain why an item was closed without being completed. They create a permanent, scannable record of decisions.

### Area — The "which layer"
Area labels are deliberately broad — they map to universal software layers that apply to any tech stack. They answer "which part of the codebase?" without being project-specific.

---

## Usage Guidelines

### Combining Labels

Labels from different categories can be combined freely. A typical open issue might have:
- One `Type` label (what kind of work)
- One `Status` label (current state)
- One `Area` label (which layer)
- Optionally one `Community` label (contributor signal)

### Status Progression

A typical issue lifecycle:
```
opened → needs triage → ready → [work begins] → closed
```

Or with blockers:
```
needs triage → blocked → ready → [work begins] → closed
```

### Using Resolution Labels

Apply resolution labels **before closing** an issue that isn't being completed:
```
duplicate → close
invalid   → close
wontfix   → close
```

---

## AI Integration

Add Clean Labels awareness to AI coding assistants.

### GitHub Copilot

Add to `.github/copilot-instructions.md`:

```markdown
## GitHub Labels

This project uses the Clean Labels convention.
See: https://github.com/wgtechlabs/clean-labels

Labels follow the format: [Category] Description [scope]
Categories: Type, Status, Community, Resolution, Area
```

---

## Learn More

- 📋 [**SPECIFICATION.md**](SPECIFICATION.md) — Full technical specification with format rules and design rationale
- 📄 [**QUICK-REFERENCE.md**](QUICK-REFERENCE.md) — Single-page cheatsheet for quick lookup
- 🛠️ [**github-labels-template**](https://github.com/warengonzaga/github-labels-template) — CLI tool to apply Clean Labels to any repo

---

## Contributing

We welcome contributions! Please read our [Contributing Guidelines](CONTRIBUTING.md) to get started.

---

## License

MIT License — see the [LICENSE](LICENSE) file for details.

---

## Credits

Created with ❤️ by **[Waren Gonzaga](https://github.com/warengonzaga)** / **[WG Tech Labs](https://github.com/wgtechlabs)**

---

<p align="center">
  <strong>Clean Repos deserve Clean Labels.</strong>
</p>
