# Contributing Guide

Thank you for contributing to the Support Tool

This project interacts with customer databases, so **stability, safety, and clarity** are the top priorities.

Please follow these guidelines to keep the codebase clean, maintainable, and safe.

---

## ⚠️ Architecture (VERY IMPORTANT)

Always follow this flow:

```text
UI → Service → Repository → Database
```

### Rules

* ❌ Do NOT put business logic inside the UI
* ❌ Do NOT put business logic inside repositories
* ✅ Business logic belongs in **services**
* ✅ Repositories should ONLY handle database access
* ✅ UI should ONLY collect input and display results

Breaking this pattern will make the project harder to maintain.

---

## Code Style

* Prefer clear, descriptive names
* Keep functions small and focused
* Avoid large files (>500–700 lines)
* Follow Ruff suggestions
* Remove unused imports and dead code

**Readable code > clever code**

---

## Pull Requests

Before opening a PR, make sure that:

* [ ] The project starts correctly
* [ ] Ruff reports no errors
* [ ] Existing functionality is not broken
* [ ] The CHANGELOG is updated when relevant

### PR Description

Always explain:

* **What** you changed
* **Why** you changed it
* **How** it can be tested

Small, focused PRs are strongly preferred over large ones.

---

## Branch Strategy

* `main` → stable, production-ready
* `feature/...` → new features
* `fix/...` → bug fixes
* `refactor/...` → code improvements

### Examples

```text
feature/subscription-extension
fix/date-calculation
refactor/subscription-service
```

Avoid committing directly to `main`.

---

## Database Rules

🚨 **Never commit real databases.**

If sample data is needed:

* Use seed scripts
* Provide anonymized data
* Never upload customer files

---

## Safety First

This tool modifies customer databases.

Our main goal is to:

👉 **Prevent human errors**
👉 **Ensure safe operations**
👉 **Maintain traceability**

When implementing features:

* Prefer explicit confirmations for dangerous actions
* Ensure backups run before critical operations
* Log important actions
* Handle errors gracefully

If something feels risky, add a safeguard.

---

## Logging & Errors

* Log meaningful events (not noise)
* Never log passwords or sensitive data
* Show user-friendly error messages
* Keep technical details available for debugging

---

## General Principle

When in doubt, choose the solution that is:

* safer
* clearer
* easier to maintain

—not the smartest or shortest one.

---

Thank you for helping keep this project reliable and professional 🚀
