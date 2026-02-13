# Website Portal

Portal web/docs do `codex-workflows`, construido com VitePress.

Idiomas:

- English (default)
- Portugues (Brasil) em `/pt/`
- Espanol em `/es/`
- Francais em `/fr/`
- 中文 em `/zh/`

## Rodar localmente

```bash
cd website
npm install
npm run docs:dev
```

## Build

```bash
npm run docs:build
```

## Preview de producao

```bash
npm run docs:preview
```

## Deploy

Deploy automatico por GitHub Actions em `.github/workflows/docs.yml`.
Publicacao no branch `gh-pages`.
