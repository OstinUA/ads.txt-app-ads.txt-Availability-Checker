Contributing Guide
==================

## 1. Introduction

Thank you for your interest in contributing to this project.

This repository hosts a Chrome extension that estimates website traffic and top-country distribution using a Similarweb-compatible RapidAPI provider. Contributions are welcome across bug fixes, reliability improvements, developer experience, documentation, and feature development.

To keep review cycles efficient and maintain quality, please follow this guide before opening an issue or pull request.

## 2. I Have a Question

The GitHub issue tracker is reserved for:

- Reproducible defects.
- Actionable feature requests.

Please do **not** open issues for general usage or support questions.

Use one of these channels for questions instead:

- GitHub Discussions (preferred for project-specific Q&A).
- Stack Overflow (tag your question with relevant Chrome extension / JavaScript tags).
- Any dedicated community channel maintained by the project (if available).

When asking a question, include context such as the extension version, target site/domain, and what you already tried.

## 3. Reporting Bugs

A high-quality bug report should enable a maintainer to reproduce the issue quickly and consistently.

### Before opening a bug

- Search open issues for duplicates first.
- If a similar report exists, add reproducible details there instead of opening a new issue.

### Required bug report content

1. **Environment**
   - Operating system and version (e.g., Windows 11 23H2, macOS 14.6, Ubuntu 24.04).
   - Browser and version (e.g., Chrome 124.0.x).
   - Extension version (`manifest.json` -> `version`).
   - Runtime/toolchain version if relevant (e.g., Node.js version used for local checks).

2. **Steps to reproduce**
   - Provide an explicit, deterministic sequence.
   - Include domain input values and option toggles (e.g., mock mode enabled/disabled).
   - If API-related, include non-sensitive request context (base URL, endpoint path, host header).

3. **Expected behavior**
   - Describe what should have happened.

4. **Actual behavior**
   - Describe what happened instead.
   - Include exact error text and console output when available.

5. **Evidence**
   - Screenshots or short recordings for UI defects.
   - Redacted logs/network traces for API defects.

### Bug report quality checklist

- Reproducible on current `main` branch.
- Clear expected vs. actual outcome.
- No secrets included (never share API keys or personal data).

## 4. Suggesting Enhancements

Enhancement proposals should be concrete and implementation-oriented.

### What to include

- **Problem statement**: What specific limitation or pain point exists today?
- **Justification**: Why this change is needed and who benefits.
- **Use cases**: Real-world scenarios demonstrating how the feature is used.
- **Proposed behavior**: UX/API impact, configuration changes, and edge cases.
- **Alternatives considered**: Competing approaches and tradeoffs.

### Scope guidance

- Keep proposals focused and modular.
- Split broad architectural changes into staged milestones when possible.

## 5. Local Development / Setup

This repository is a plain JavaScript Chrome extension with no package manager manifest committed.

### Fork and clone

```bash
git clone https://github.com/<your-username>/Traffic-Stats-Analyzer.git
cd Traffic-Stats-Analyzer
git remote add upstream https://github.com/<upstream-owner>/Traffic-Stats-Analyzer.git
```

### Dependencies

No npm/pip dependency install step is currently required.

### Environment variables

No `.env` file is used by default.

The extension stores provider configuration (including API key) via Chrome storage from the Options panel at runtime. Keep secrets out of commits and screenshots.

### Run locally

1. Open `chrome://extensions`.
2. Enable **Developer mode**.
3. Click **Load unpacked**.
4. Select the repository root directory.
5. Pin the extension and test via the popup/options UI.

### Optional local validation commands

```bash
node --check background/service-worker.js
node --check popup/popup.js
node --check options/options.js
node --check shared/constants.js
node --check shared/domain.js
node --check shared/mock-data.js
```

## 6. Pull Request Process

### Branching strategy

Create branches from `main` using these prefixes:

- `feature/<short-kebab-name>` for new functionality.
- `bugfix/<issue-number-or-short-kebab-name>` for defect fixes.
- `docs/<short-kebab-name>` for documentation-only changes.
- `chore/<short-kebab-name>` for maintenance tasks.

### Commit messages

Use Conventional Commits:

- `feat: add configurable fallback source label`
- `fix: handle missing host header in provider settings`
- `docs: add API response envelope examples`
- `chore: normalize extension metadata`

### Upstream synchronization

Before opening or updating a PR, sync with upstream `main`:

```bash
git fetch upstream
git checkout main
git rebase upstream/main
git checkout <your-branch>
git rebase main
```

### PR description requirements

Every PR must include:

- Linked issue(s) (e.g., `Closes #123`) where applicable.
- Context and motivation.
- Summary of implementation details.
- Test coverage proof (commands and results).
- Screenshots/GIFs for visible UI changes.
- Risk notes and rollback considerations for behavior changes.

## 7. Styleguides

### Code style

- Use modern ES module syntax already used in the repository.
- Preserve current naming conventions:
  - `camelCase` for variables/functions.
  - `UPPER_SNAKE_CASE` for constants.
- Keep functions cohesive and side-effect boundaries explicit.
- Avoid unrelated refactors in focused PRs.

### Formatting and linting tools

- **ESLint**: not configured in this repository today.
- **Prettier**: not configured in this repository today.
- **Black / Flake8**: not applicable (no Python codebase).

Contributors should keep formatting consistent with surrounding files and avoid stylistic churn.

### Architectural conventions

- Shared cross-context utilities live in `shared/`.
- Background integration and API orchestration live in `background/service-worker.js`.
- UI concerns remain in `popup/` and `options/`.
- Keep API contract constants centralized in `shared/constants.js`.

## 8. Testing

All bug fixes and new features must include relevant validation.

### Minimum expectations

- Add or update tests when a test harness exists for the changed behavior.
- At minimum, run syntax checks and manual extension smoke tests for impacted flows.

### Local test commands

```bash
node --check background/service-worker.js
node --check popup/popup.js
node --check options/options.js
node --check shared/constants.js
node --check shared/domain.js
node --check shared/mock-data.js
```

### Manual verification checklist

- Extension loads without runtime errors in `chrome://extensions`.
- Popup `Analyze` flow works for at least one valid domain.
- Options save/load behavior works.
- Mock mode and fallback behavior remain functional.

## 9. Code Review Process

After a PR is opened:

1. Maintainers triage for scope, quality, and project fit.
2. CI or required checks (if configured) must pass.
3. At least **1 maintainer approval** is required before merge.
4. Authors must address all blocking feedback and push updates.
5. After updates, authors should re-request review.

### Review expectations

- Keep discussions technical and specific.
- Resolve conversations only after changes are applied or rationale is accepted.
- If requirements change during review, update PR description accordingly.

### Merge criteria

A PR can be merged when:

- Required approvals are present.
- Requested changes are resolved.
- No unresolved blockers remain.
- Branch is up to date with `main` (or rebased as requested by maintainers).
