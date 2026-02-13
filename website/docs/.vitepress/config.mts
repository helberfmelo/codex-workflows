import { defineConfig } from "vitepress";

const enNav = [
  { text: "Home", link: "/" },
  { text: "Install", link: "/get-started/installation" },
  { text: "Workflows", link: "/reference/workflows" },
  { text: "Release", link: "/reference/release" },
  { text: "Examples", link: "/reference/examples" },
  { text: "PT-BR", link: "/pt/" },
  { text: "GitHub", link: "https://github.com/helberfmelo/codex-workflows" }
];

const ptNav = [
  { text: "Inicio", link: "/pt/" },
  { text: "Instalacao", link: "/pt/get-started/installation" },
  { text: "Workflows", link: "/pt/reference/workflows" },
  { text: "Release", link: "/pt/reference/release" },
  { text: "Exemplos", link: "/pt/reference/examples" },
  { text: "EN", link: "/" },
  { text: "GitHub", link: "https://github.com/helberfmelo/codex-workflows" }
];

const enSidebar = [
  {
    text: "Get Started",
    items: [
      { text: "Overview", link: "/" },
      { text: "Installation", link: "/get-started/installation" },
      { text: "Quickstart", link: "/get-started/quickstart" }
    ]
  },
  {
    text: "Reference",
    items: [
      { text: "Workflows", link: "/reference/workflows" },
      { text: "Packs", link: "/reference/packs" },
      { text: "Operations", link: "/reference/operations" },
      { text: "Release", link: "/reference/release" },
      { text: "Composer", link: "/reference/composer" },
      { text: "Examples", link: "/reference/examples" },
      { text: "Source Docs", link: "/reference/source" }
    ]
  },
  {
    text: "Strategy",
    items: [{ text: "Monetization", link: "/strategy/monetization" }]
  }
];

const ptSidebar = [
  {
    text: "Comece Aqui",
    items: [
      { text: "Visao Geral", link: "/pt/" },
      { text: "Instalacao", link: "/pt/get-started/installation" },
      { text: "Quickstart", link: "/pt/get-started/quickstart" }
    ]
  },
  {
    text: "Referencia",
    items: [
      { text: "Workflows", link: "/pt/reference/workflows" },
      { text: "Packs", link: "/pt/reference/packs" },
      { text: "Operacoes", link: "/pt/reference/operations" },
      { text: "Release", link: "/pt/reference/release" },
      { text: "Composer", link: "/pt/reference/composer" },
      { text: "Exemplos", link: "/pt/reference/examples" },
      { text: "Documentos Fonte", link: "/pt/reference/source" }
    ]
  },
  {
    text: "Estrategia",
    items: [{ text: "Monetizacao", link: "/pt/strategy/monetization" }]
  }
];

export default defineConfig({
  title: "Codex Workflows",
  description: "Workflow operating system for GPT Codex in VS Code.",
  base: process.env.DOCS_BASE || "/codex-workflows/",
  lastUpdated: true,
  cleanUrls: true,
  head: [
    ["meta", { name: "theme-color", content: "#0f5f87" }],
    ["meta", { property: "og:title", content: "Codex Workflows Docs" }],
    ["meta", { property: "og:description", content: "Professional docs portal for VS Code + GPT Codex workflows." }]
  ],
  locales: {
    root: {
      label: "English",
      lang: "en-US",
      themeConfig: {
        logo: "/logo-mark.svg",
        nav: enNav,
        sidebar: enSidebar,
        socialLinks: [{ icon: "github", link: "https://github.com/helberfmelo/codex-workflows" }],
        search: { provider: "local" },
        footer: {
          message: "MIT License",
          copyright: "Copyright 2026 codex-workflows contributors"
        }
      }
    },
    pt: {
      label: "Portugues (Brasil)",
      lang: "pt-BR",
      link: "/pt/",
      themeConfig: {
        logo: "/logo-mark.svg",
        nav: ptNav,
        sidebar: ptSidebar,
        socialLinks: [{ icon: "github", link: "https://github.com/helberfmelo/codex-workflows" }],
        search: { provider: "local" },
        footer: {
          message: "Licenca MIT",
          copyright: "Copyright 2026 contribuidores do codex-workflows"
        }
      }
    }
  }
});
