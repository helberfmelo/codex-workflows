# Composer Integration

Composer is optional and mainly useful for PHP-first teams that standardize installs through Composer scripts.

## Is Composer required?

No. The official installation path remains the Codex `skill-installer` command.

## What is supported?

This repository includes:

- `composer.json` with installer scripts;
- `scripts/composer_install.php` wrapper to call the official Python installer.

## Commands

Install full suite (core + all packs):

```bash
composer codex:install-all
```

Install only core workflow skill:

```bash
composer codex:install-core
```

Custom ref:

```bash
composer codex:install-all -- --ref=v1.1.0
```

## Notes

- Composer commands still depend on Python and Codex home tooling.
- This channel is a convenience wrapper, not a separate installer implementation.
