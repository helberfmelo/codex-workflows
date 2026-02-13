# Integracao com Composer

Composer e opcional, pensado para times PHP que querem padronizar a instalacao via scripts Composer.

## E obrigatorio usar Composer?

Nao. O canal oficial continua sendo o `skill-installer` do Codex.

## O que este repositorio oferece?

- `composer.json` com scripts de instalacao;
- `scripts/composer_install.php` que chama o instalador Python oficial.

## Comandos

Instalar suite completa:

```bash
composer codex:install-all
```

Instalar apenas core:

```bash
composer codex:install-core
```

Usar tag/ref especifica:

```bash
composer codex:install-all -- --ref=v1.1.0
```
