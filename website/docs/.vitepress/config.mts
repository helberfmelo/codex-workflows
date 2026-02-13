import { defineConfig } from "vitepress";

const enNav = [
  { text: "Home", link: "/" },
  { text: "Install", link: "/get-started/installation" },
  { text: "Workflows", link: "/reference/workflows" },
  { text: "Examples", link: "/reference/examples" }
];

const ptNav = [
  { text: "Inicio", link: "/pt/" },
  { text: "Instalacao", link: "/pt/get-started/installation" },
  { text: "Workflows", link: "/pt/reference/workflows" },
  { text: "Exemplos", link: "/pt/reference/examples" }
];

const esNav = [
  { text: "Inicio", link: "/es/" },
  { text: "Instalacion", link: "/es/get-started/installation" },
  { text: "Workflows", link: "/es/reference/workflows" },
  { text: "Ejemplos", link: "/es/reference/examples" }
];

const frNav = [
  { text: "Accueil", link: "/fr/" },
  { text: "Installation", link: "/fr/get-started/installation" },
  { text: "Workflows", link: "/fr/reference/workflows" },
  { text: "Exemples", link: "/fr/reference/examples" }
];

const zhNav = [
  { text: "首页", link: "/zh/" },
  { text: "安装", link: "/zh/get-started/installation" },
  { text: "工作流", link: "/zh/reference/workflows" },
  { text: "示例", link: "/zh/reference/examples" }
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

const esSidebar = [
  {
    text: "Primeros Pasos",
    items: [
      { text: "Vision General", link: "/es/" },
      { text: "Instalacion", link: "/es/get-started/installation" },
      { text: "Quickstart", link: "/es/get-started/quickstart" }
    ]
  },
  {
    text: "Referencia",
    items: [
      { text: "Workflows", link: "/es/reference/workflows" },
      { text: "Packs", link: "/es/reference/packs" },
      { text: "Operaciones", link: "/es/reference/operations" },
      { text: "Release", link: "/es/reference/release" },
      { text: "Composer", link: "/es/reference/composer" },
      { text: "Ejemplos", link: "/es/reference/examples" },
      { text: "Documentos Fuente", link: "/es/reference/source" }
    ]
  },
  {
    text: "Estrategia",
    items: [{ text: "Monetizacion", link: "/es/strategy/monetization" }]
  }
];

const frSidebar = [
  {
    text: "Demarrage",
    items: [
      { text: "Vue d'ensemble", link: "/fr/" },
      { text: "Installation", link: "/fr/get-started/installation" },
      { text: "Quickstart", link: "/fr/get-started/quickstart" }
    ]
  },
  {
    text: "Reference",
    items: [
      { text: "Workflows", link: "/fr/reference/workflows" },
      { text: "Packs", link: "/fr/reference/packs" },
      { text: "Operations", link: "/fr/reference/operations" },
      { text: "Release", link: "/fr/reference/release" },
      { text: "Composer", link: "/fr/reference/composer" },
      { text: "Exemples", link: "/fr/reference/examples" },
      { text: "Docs Source", link: "/fr/reference/source" }
    ]
  },
  {
    text: "Strategie",
    items: [{ text: "Monetisation", link: "/fr/strategy/monetization" }]
  }
];

const zhSidebar = [
  {
    text: "快速开始",
    items: [
      { text: "总览", link: "/zh/" },
      { text: "安装", link: "/zh/get-started/installation" },
      { text: "快速上手", link: "/zh/get-started/quickstart" }
    ]
  },
  {
    text: "参考",
    items: [
      { text: "工作流", link: "/zh/reference/workflows" },
      { text: "Packs", link: "/zh/reference/packs" },
      { text: "运维", link: "/zh/reference/operations" },
      { text: "发布", link: "/zh/reference/release" },
      { text: "Composer", link: "/zh/reference/composer" },
      { text: "示例", link: "/zh/reference/examples" },
      { text: "源文档", link: "/zh/reference/source" }
    ]
  },
  {
    text: "策略",
    items: [{ text: "商业化", link: "/zh/strategy/monetization" }]
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
      label: "EN",
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
      label: "PT-BR",
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
    },
    es: {
      label: "ES",
      lang: "es-ES",
      link: "/es/",
      themeConfig: {
        logo: "/logo-mark.svg",
        nav: esNav,
        sidebar: esSidebar,
        socialLinks: [{ icon: "github", link: "https://github.com/helberfmelo/codex-workflows" }],
        search: { provider: "local" },
        footer: {
          message: "Licencia MIT",
          copyright: "Copyright 2026 contribuidores de codex-workflows"
        }
      }
    },
    fr: {
      label: "FR",
      lang: "fr-FR",
      link: "/fr/",
      themeConfig: {
        logo: "/logo-mark.svg",
        nav: frNav,
        sidebar: frSidebar,
        socialLinks: [{ icon: "github", link: "https://github.com/helberfmelo/codex-workflows" }],
        search: { provider: "local" },
        footer: {
          message: "Licence MIT",
          copyright: "Copyright 2026 contributeurs codex-workflows"
        }
      }
    },
    zh: {
      label: "ZH",
      lang: "zh-CN",
      link: "/zh/",
      themeConfig: {
        logo: "/logo-mark.svg",
        nav: zhNav,
        sidebar: zhSidebar,
        socialLinks: [{ icon: "github", link: "https://github.com/helberfmelo/codex-workflows" }],
        search: { provider: "local" },
        footer: {
          message: "MIT 许可证",
          copyright: "Copyright 2026 codex-workflows contributors"
        }
      }
    }
  }
});
