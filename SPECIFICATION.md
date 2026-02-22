# Clean Labels Specification

Version: 1.0.0

This document provides the complete technical specification for the Clean Labels convention.

**About this convention:** Clean Labels is a standardized GitHub label naming, color, and description system developed from real-world open source practice. It provides a consistent, opinionated set of labels that any project can adopt.

---

## Table of Contents

- [Convention Format](#convention-format)
- [The 5 Categories](#the-5-categories)
- [Full Label Reference](#full-label-reference)
- [Color Palette](#color-palette)
- [Design Principles](#design-principles)
- [Combining Labels](#combining-labels)
- [Edge Cases & FAQs](#edge-cases--faqs)
- [Comparison with GitHub Defaults](#comparison-with-github-defaults)

---

## Convention Format

### Label Name

Label names are:
- **Lowercase** — always
- **Space-separated** — use spaces, not hyphens or underscores (e.g., `good first issue`, not `good-first-issue`)
- **Concise** — one or two words preferred; three words maximum for community labels
- **No emoji prefix** — names are plain text

### Label Description

Every description follows this exact structure:

```
[Category] Description [scope]
```

**Components:**
1. **`[Category]`** — The category tag in square brackets. Exactly one of: `Type`, `Status`, `Community`, `Resolution`, `Area`
2. **Description** — Plain English. Sentence-style (capitalize first word only where needed). No period at the end.
3. **`[scope]`** — The applicable scope in square brackets. Exactly one of:
   - `[issues]` — applies only to issues
   - `[PRs]` — applies only to pull requests
   - `[issues, PRs]` — applies to both

**Example:**
```
[Type] Something isn't working [issues, PRs]
```

### Label Color

Colors are:
- **Expressed as 6-character hex** without the `#` prefix in API contexts
- **Category-aware** — related labels within a category share a visual family
- **Purposeful** — colors carry semantic meaning (red for blocking/critical, green for positive/ready, gray for closed/resolved)

---

## The 5 Categories

### Type

Classifies **what kind of work** this item represents. Every issue or PR should have exactly one Type label.

- Applies to both issues and PRs unless noted
- Describes the nature of the work, not its state
- Immutable — a bug doesn't stop being a bug because it's blocked

### Status

Tracks **where in the workflow** an item currently sits. Optional but highly recommended for open issues.

- Applies only to issues (workflow state is tracked differently for PRs)
- Mutable — update as the item moves through the process
- Only one Status label should be active at a time

### Community

Signals **contributor intent** for open source projects. Optional.

- Primarily applies to issues (with exceptions for maintainer-only PRs)
- Helps contributors find work appropriate for them
- Can coexist with other category labels

### Resolution

Explains **why an item was closed** without being completed. Applied at close time.

- Applies to both issues and PRs
- Replaces Status labels when closing
- Mutually exclusive — only one Resolution label per item

### Area

Marks **which layer of the codebase** is affected. Optional but useful for filtering.

- Applies to both issues and PRs
- Based on universal software layers (not project-specific)
- Multiple Area labels are acceptable for cross-cutting concerns

---

## Full Label Reference

### Type Labels

| Name | Color | Full Description |
|------|-------|-----------------|
| `bug` | `d73a4a` | `[Type] Something isn't working [issues, PRs]` |
| `enhancement` | `1a7f37` | `[Type] New feature or improvement to existing functionality [issues, PRs]` |
| `documentation` | `0075ca` | `[Type] Improvements or additions to docs, README, or guides [issues, PRs]` |
| `refactor` | `8957e5` | `[Type] Code improvement without changing functionality [PRs]` |
| `performance` | `e3795c` | `[Type] Optimization, speed, or resource usage improvements [issues, PRs]` |
| `security` | `d4a72c` | `[Type] Security vulnerability or hardening [issues, PRs]` |

### Status Labels

| Name | Color | Full Description |
|------|-------|-----------------|
| `blocked` | `cf222e` | `[Status] Waiting on another issue, decision, or external factor [issues]` |
| `needs triage` | `e16f24` | `[Status] New issue — needs review and categorization [issues]` |
| `awaiting response` | `1a7ec7` | `[Status] Waiting for more information from the reporter [issues]` |
| `ready` | `2da44e` | `[Status] Triaged and ready to be picked up [issues]` |

### Community Labels

| Name | Color | Full Description |
|------|-------|-----------------|
| `good first issue` | `7057ff` | `[Community] Good for newcomers — well-scoped and documented [issues]` |
| `help wanted` | `0e8a16` | `[Community] Open for community contribution [issues]` |
| `maintainer only` | `b60205` | `[Community] Reserved for maintainers — not open for external contribution [issues, PRs]` |

### Resolution Labels

| Name | Color | Full Description |
|------|-------|-----------------|
| `duplicate` | `cfd3d7` | `[Resolution] This issue or pull request already exists [issues, PRs]` |
| `invalid` | `cfd3d7` | `[Resolution] This doesn't seem right [issues, PRs]` |
| `wontfix` | `cfd3d7` | `[Resolution] This will not be worked on [issues]` |

### Area Labels

| Name | Color | Full Description |
|------|-------|-----------------|
| `core` | `0052cc` | `[Area] Core logic, business rules, and primary functionality [issues, PRs]` |
| `interface` | `5319e7` | `[Area] User-facing layer — UI, CLI, API endpoints, or SDK surface [issues, PRs]` |
| `data` | `006b75` | `[Area] Database, storage, caching, or data models [issues, PRs]` |
| `infra` | `e16f24` | `[Area] Build system, CI/CD, deployment, config, and DevOps [issues, PRs]` |
| `testing` | `1a7f37` | `[Area] Unit tests, integration tests, E2E, and test tooling [issues, PRs]` |

---

## Color Palette

### Color Assignments by Category

| Category | Color Strategy |
|----------|---------------|
| **Type** | Distinct colors per label — semantic (red for bugs, green for enhancements, etc.) |
| **Status** | Traffic light progression — red (blocked), orange (needs triage), blue (awaiting), green (ready) |
| **Community** | Distinct colors — red for restricted, purple for newcomer, green for open |
| **Resolution** | Uniform gray `cfd3d7` — all resolution labels look the same intentionally |
| **Area** | Blues and teals — cool tones to distinguish from action-oriented labels |

### Full Color Reference

| Hex | Used By |
|-----|---------|
| `d73a4a` | `bug` |
| `1a7f37` | `enhancement`, `testing` |
| `0075ca` | `documentation` |
| `8957e5` | `refactor` |
| `e3795c` | `performance` |
| `d4a72c` | `security` |
| `cf222e` | `blocked` |
| `e16f24` | `needs triage`, `infra` |
| `1a7ec7` | `awaiting response` |
| `2da44e` | `ready` |
| `7057ff` | `good first issue` |
| `0e8a16` | `help wanted` |
| `b60205` | `maintainer only` |
| `cfd3d7` | `duplicate`, `invalid`, `wontfix` |
| `0052cc` | `core` |
| `5319e7` | `interface` |
| `006b75` | `data` |

---

## Design Principles

### 1. Every label has a category

The `[Category]` prefix in every description ensures that even when you're looking at a filtered list or export, you always know what a label means. No ambiguity.

### 2. Scope is explicit

The `[scope]` suffix tells you exactly where a label applies. `[issues]` labels should never appear on PRs. This creates a discipline that makes your label usage consistent.

### 3. Resolution labels are gray on purpose

All three resolution labels share the same gray color. This signals "this item is done — categorization matters less than closure." The uniformity also prevents color fatigue in large issue trackers.

### 4. Area labels are universal

Area labels map to software layers that exist in every project: core logic, user interface, data/storage, infrastructure, and testing. They avoid framework or language-specific names that would make the convention non-portable.

### 5. No hacktoberfest labels in core

Hacktoberfest labels are event-specific and time-limited. They are not part of the core Clean Labels set. Use the [github-labels-template](https://github.com/warengonzaga/github-labels-template) CLI with the `generate` command or add them manually when participating in the event.

### 6. 21 is the ceiling

Clean Labels deliberately avoids label sprawl. 21 labels cover every common workflow need. Adding custom labels should be the exception, not the norm.

---

## Combining Labels

### Recommended Combinations

**Typical open issue:**
```
enhancement + needs triage + interface
```

**Issue ready for contributors:**
```
bug + ready + core + good first issue
```

**Security vulnerability:**
```
security + ready + core
```

**Closed as resolved:**
```
bug + duplicate → close
```

### Rules for Combining

1. **One Type label** — an issue is one kind of thing
2. **One Status label** — an issue is in one state at a time
3. **One Community label** — clear contributor signal
4. **One Resolution label** — one reason for closure
5. **Multiple Area labels allowed** — cross-cutting concerns are real

### What Not to Combine

❌ Two Type labels: `bug` + `enhancement`  
❌ Two Status labels: `blocked` + `ready`  
❌ Status + Resolution: `needs triage` + `duplicate`  
❌ `good first issue` + `maintainer only`

---

## Edge Cases & FAQs

### Q: What if my issue is both a bug and a documentation problem?

**A:** Choose the primary nature. If the root cause is a code bug, use `bug`. If it's a missing or incorrect doc, use `documentation`. When in doubt, create two separate issues.

### Q: Can I use Area labels on issues that span multiple layers?

**A:** Yes. Multiple Area labels are explicitly allowed. A security issue that affects both `core` and `interface` should have both.

### Q: When does `refactor` apply to issues vs. PRs only?

**A:** The `refactor` label has scope `[PRs]` because refactoring is typically planned and executed as a PR, not tracked as an issue in most workflows. If your team tracks refactoring work as issues, applying it there is acceptable.

### Q: Should every issue have a Status label?

**A:** Recommended, but not required. At minimum, use `needs triage` when issues are first opened. The `ready` label is especially valuable for open source projects where contributors need to know what's safe to pick up.

### Q: Can I add custom labels?

**A:** Yes. Clean Labels defines the core 21. You can add project-specific labels alongside them. The convention only governs the core set — your custom labels should follow the same description format for consistency.

### Q: What about `hacktoberfest` labels?

**A:** Hacktoberfest labels are intentionally excluded from the core set because they're event-specific and time-bounded. The [github-labels-template](https://github.com/warengonzaga/github-labels-template) tool includes them as optional community labels that you can apply when participating.

---

## Comparison with GitHub Defaults

GitHub creates 9 default labels for every new repository. Here's how they map to Clean Labels:

| GitHub Default | Clean Labels Equivalent | Notes |
|---------------|------------------------|-------|
| `bug` | `bug` | Same name, standardized description |
| `documentation` | `documentation` | Same name, standardized description |
| `duplicate` | `duplicate` | Same name, standardized description |
| `enhancement` | `enhancement` | Same name, standardized description |
| `good first issue` | `good first issue` | Same name, standardized description |
| `help wanted` | `help wanted` | Same name, standardized description |
| `invalid` | `invalid` | Same name, standardized description |
| `question` | *(not included)* | Use `awaiting response` for the workflow intent |
| `wontfix` | `wontfix` | Same name, standardized description |

**What Clean Labels adds:**
- `refactor`, `performance`, `security` (new Type labels)
- `blocked`, `needs triage`, `ready` (full Status lifecycle)
- `maintainer only` (Community clarity)
- `core`, `interface`, `data`, `infra`, `testing` (Area layer)

**What Clean Labels removes:**
- `question` — replaced by `awaiting response` which is more specific

---

*For quick reference, see [QUICK-REFERENCE.md](QUICK-REFERENCE.md)*
