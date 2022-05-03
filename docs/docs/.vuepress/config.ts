import { path } from '@vuepress/utils'
// import { defaultTheme } from "@vuepress/theme-default"
import { searchPlugin } from "@vuepress/plugin-search"
import { defaultTheme, defineUserConfig } from 'vuepress'


export default defineUserConfig({
  // title: "pyuse文档",
  description: "a python3 wheels library",
  base: "/pyuse/",
  locales: {
    "/": {
      lang: "en-US",
      title: "pyuse docs",
      description: "A python3 wheels library, OOTB, Kinda Interesting",
    },
    "/zh/": {
      lang: "中文",
      title: "pyuse文档",
      description:
        "一个 python3 的库。比较完整, 开箱即用, 有点意思",
    },
  },
  plugins: [
    searchPlugin({
      locales: {
        "/": {
          placeholder: "Search",
        },
        "/zh/": {
          placeholder: "搜索",
        },
      },
      isSearchable: (page) => page.path !== "/",
    }),
  ],
  theme: defaultTheme({
    repo: "yongchin0821/pyuse",
    docsBranch: "main/docs/docs",
    locales: {
      "/": {
        navbar: [{ text: "guide", link: "/guide/introduce" }],
        sidebar: [
          {
            text: "Guide",
            children: ["/guide/introduce", "/guide/quick_start"],
          },
          {
            text: "Core Functions",
            children: [
              "/api/useDingTalk",
              "/api/useGenerator",
              "/api/usePath",
              "/api/useTime",
            ],
          },
        ],
      },
      "/zh/": {
        navbar: [{ text: "指南", link: "/zh/guide/introduce" }],
        sidebar: [
          {
            text: "指南",
            children: ["/zh/guide/introduce", "/zh/guide/quick_start"],
          },
          {
            text: "核心功能",
            children: [
              "/zh/api/useDingTalk",
              "/zh/api/useGenerator",
              "/zh/api/usePath",
              "/zh/api/useTime",
            ],
          },
        ],
      },
    },
    editLinks: true,
    editLinkText: "在 GitHub 上编辑此页",
    lastUpdated: true,
    lastUpdatedText: "上次更新",
  }),
  alias: {
    '@theme/HomeHero.vue': path.resolve(__dirname, './components/Home.vue'),
  },
})
