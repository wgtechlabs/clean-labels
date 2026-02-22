# Clean Labels Quick Reference

**One-page cheatsheet for the Clean Labels convention**

---

## Convention Format

```
[Category] Description [scope]
```

- **Category**: `Type` | `Status` | `Community` | `Resolution` | `Area`
- **Scope**: `[issues]` | `[PRs]` | `[issues, PRs]`

---

## All 21 Labels

### Type — What kind of work?

| Name | Color | Scope |
|------|-------|-------|
| `bug` | `#d73a4a` | issues, PRs |
| `enhancement` | `#1a7f37` | issues, PRs |
| `documentation` | `#0075ca` | issues, PRs |
| `refactor` | `#8957e5` | PRs |
| `performance` | `#e3795c` | issues, PRs |
| `security` | `#d4a72c` | issues, PRs |

### Status — Where in the workflow?

| Name | Color | Scope |
|------|-------|-------|
| `blocked` | `#cf222e` | issues |
| `needs triage` | `#e16f24` | issues |
| `awaiting response` | `#1a7ec7` | issues |
| `ready` | `#2da44e` | issues |

### Community — Who should work on it?

| Name | Color | Scope |
|------|-------|-------|
| `good first issue` | `#7057ff` | issues |
| `help wanted` | `#0e8a16` | issues |
| `maintainer only` | `#b60205` | issues, PRs |

### Resolution — Why was it closed?

| Name | Color | Scope |
|------|-------|-------|
| `duplicate` | `#cfd3d7` | issues, PRs |
| `invalid` | `#cfd3d7` | issues, PRs |
| `wontfix` | `#cfd3d7` | issues |

### Area — Which layer of the codebase?

| Name | Color | Scope |
|------|-------|-------|
| `core` | `#0052cc` | issues, PRs |
| `interface` | `#5319e7` | issues, PRs |
| `data` | `#006b75` | issues, PRs |
| `infra` | `#e16f24` | issues, PRs |
| `testing` | `#1a7f37` | issues, PRs |

---

## Quick Apply

```bash
# All 21 labels (npx)
npx github-labels-template apply

# Specific category
npx github-labels-template apply --category type
npx github-labels-template apply --category status
npx github-labels-template apply --category community
npx github-labels-template apply --category resolution
npx github-labels-template apply --category area

# Specific repo
npx github-labels-template apply --repo owner/repo

# Clean slate (wipe + apply)
npx github-labels-template migrate
```

---

## Combining Labels Cheatsheet

### New issue (just opened)
```
[Type] + needs triage
```

### Issue ready for contributors
```
[Type] + ready + [Area] + good first issue
```

### Blocked issue
```
[Type] + blocked + [Area]
```

### Closing without completing
```
[Type] + duplicate → close
[Type] + invalid → close
[Type] + wontfix → close
```

---

## Combination Rules

| Rule | ✅ Do | ❌ Don't |
|------|-------|---------|
| Type | One per item | `bug` + `enhancement` |
| Status | One at a time | `blocked` + `ready` |
| Resolution | One per closure | `duplicate` + `invalid` |
| Area | Multiple OK | — |
| Status + Resolution | Never both | `needs triage` + `duplicate` |
| Community | One per item | `good first issue` + `maintainer only` |

---

## Status Lifecycle

```
opened
  └── needs triage
        ├── awaiting response
        │     └── needs triage (if info received)
        ├── blocked
        │     └── ready (when unblocked)
        └── ready
              └── [work begins → PR → close]
```

---

## Manual Label Creation (gh CLI)

```bash
gh label create "bug" --color "d73a4a" \
  --description "[Type] Something isn't working [issues, PRs]"

gh label create "needs triage" --color "e16f24" \
  --description "[Status] New issue — needs review and categorization [issues]"

gh label create "good first issue" --color "7057ff" \
  --description "[Community] Good for newcomers — well-scoped and documented [issues]"

gh label create "duplicate" --color "cfd3d7" \
  --description "[Resolution] This issue or pull request already exists [issues, PRs]"

gh label create "core" --color "0052cc" \
  --description "[Area] Core logic, business rules, and primary functionality [issues, PRs]"
```

---

## Need More Details?

- 📋 [Full Specification](SPECIFICATION.md)
- 📖 [Main README](README.md)
- 🛠️ [github-labels-template CLI](https://github.com/warengonzaga/github-labels-template)

---

<p align="center">
  <strong>Clean Repos deserve Clean Labels.</strong>
</p>
