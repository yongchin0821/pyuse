const { defaultTheme } = require("@vuepress/theme-default");
const { searchPlugin } = require("@vuepress/plugin-search");

module.exports = {
  // title: "pyuse文档",
  description: "基于unittest 的 Web UI/HTTP自动化测试框架。",
  base: "/",
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
    repo: "nickliya/pyuse",
    docsBranch: "main/docs/docs",
    locales: {
      "/": {
        navbar: [{ text: "guide", link: "/introduce" }],
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
        navbar: [{ text: "指南", link: "/introduce" }],
        sidebar: [
          {
            text: "指南",
            children: ["/guide/introduce", "/guide/quick_start"],
          },
          {
            text: "核心功能",
            children: [
              "/api/useDingTalk",
              "/api/useGenerator",
              "/api/usePath",
              "/api/useTime",
            ],
          },
        ],
      },
    },
    editLinks: true,
    editLinkText: "在 GitHub 上编辑此页",
    lastUpdated: "上次更新",
  }),
};
