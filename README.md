# quote‑cli

A single‑file Python command‑line tool that prints a random quote.

## Features
- No third‑party dependencies – just the Python standard library.
- Typed, lint‑friendly code (flake8 + mypy compatible).
- Unit tests with `pytest`.
- GitHub Actions workflow that runs lint, type‑check, tests and builds a ZIP release.
- Automatic release notes via GitHub Release.

## Usage
```bash
pip install .
quote-cli          # prints a random quote
quote-cli --list   # list all available quotes
```

## Development
```bash
# Run CI locally
make ci
```

## Fallback naming
If `quote-cli` is taken, try `quote‑cli‑tiny`, `quote‑cli‑2024`, or `quote‑cli‑{{random‑suffix}}`.
