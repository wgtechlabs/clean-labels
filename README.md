# Clean Labels

> **Clean Repos deserve Clean Labels.**

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Version](https://img.shields.io/badge/version-1.0.0-green.svg)](https://github.com/wgtechlabs/clean-labels)

A standardized GitHub label convention designed to be consistent, scannable, and universal. Clean Labels defines a curated set of labels organized into 5 clear categories — every label follows the same format so your team always knows what they're looking at.

**Note:** This is a documented convention refined through real-world open source practice. The [github-labels-template](https://github.com/warengonzaga/github-labels-template) CLI tool is the official implementation for applying Clean Labels to any repository.

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
# Apply all 21 labels to the current repo
npx github-labels-template apply

# Apply labels from a specific category
npx github-labels-template apply --category type

# Apply to a specific repo
npx github-labels-template apply --repo owner/repo
```

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
