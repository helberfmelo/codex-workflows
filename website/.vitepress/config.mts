import { defineConfig } from "vitepress";

export default defineConfig({
  title: "Codex Workflows",
  description: "Workflow operating system for GPT Codex in VS Code.",
  base: process.env.DOCS_BASE || "/codex-workflows/",
  lastUpdated: true,
  cleanUrls: true,
  themeConfig: {
    logo: "/logo-mark.svg",
    nav: [
      { text: "Home", link: "/" },
      { text: "Instalacao", link: "/get-started/installation" },
      { text: "Quickstart", link: "/get-started/quickstart" },
      { text: "Referencia", link: "/reference/workflows" },
      { text: "GitHub", link: "https://github.com/helberfmelo/codex-workflows" }
    ],
    sidebar: [
      {
        text: "Comece Aqui",
        items: [
          { text: "Visao Geral", link: "/" },
          { text: "Instalacao", link: "/get-started/installation" },
          { text: "Quickstart", link: "/get-started/quickstart" }
        ]
      },
      {
        text: "Referencia",
        items: [
          { text: "Workflows", link: "/reference/workflows" },
          { text: "Packs", link: "/reference/packs" },
          { text: "Operacoes", link: "/reference/operations" },
          { text: "Release", link: "/reference/release" },
          { text: "Exemplos", link: "/reference/examples" },
          { text: "Fonte Tecnica", link: "/reference/source" }
        ]
      },
      {
        text: "Estrategia",
        items: [{ text: "Monetizacao", link: "/strategy/monetization" }]
      }
    ],
    socialLinks: [{ icon: "github", link: "https://github.com/helberfmelo/codex-workflows" }],
    search: {
      provider: "local"
    },
    footer: {
      message: "MIT License",
      copyright: "Copyright 2026 codex-workflows contributors"
    }
  },
  head: [
    ["meta", { name: "theme-color", content: "#165d7d" }],
    ["meta", { property: "og:title", content: "Codex Workflows" }],
    ["meta", { property: "og:description", content: "Workflow operating system for GPT Codex in VS Code." }]
  ]
});
