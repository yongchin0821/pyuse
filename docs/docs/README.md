## ☘️Introduction

基于 vuepress2.0+ 的 **pyuse [操作文档](https://yongchin0821.github.io/pyuse/)**

首页的部分样式 [参考了这里](https://github.com/mx-space/docs)

你可以使用 Markdown 书写文档，并通过 VuePress 部署为可预览的页面。

## 📖使用说明

### 1. 安装

1. clone本项目并安装依赖

```bash
git clone https://github.com/yongchin0821/pyuse.git
cd docs
yarn install
```

### 2. 开发

正式开发前，可以先阅读 [VuePress官方文档](https://v2.vuepress.vuejs.org/zh/)。

在`docs/docs`文件夹内，修改你想修改的`.md`文档并保存。

然后执行以下命令进行预览或打包

```bash
yarn run dev # 预览
yarn run build # 生成静态页面
```

## 部署

**Github-Pages手动本地部署部署说明：**

本地进入项目中执行`deploy.sh`即可自动部署到github pages。

deploy.sh 的详情如下（**请自行判断启用注释掉的命令**）:

```shell
#!/usr/bin/env sh
# 确保脚本抛出遇到的错误
set -e

# 生成静态文件
npm run build

# 进入生成的文件夹
cd vpdocs/.vuepress/dist

git init
git add -A
git commit -m 'deploy'

# 如果发布到 https://SeldomQA.github.io
git push -f https://github.com/yongchin0821/pyuse.git main:gh-pages

cd -
```

更多部署方式可以参阅 [VuePress文档|部署](https://v1.vuepress.vuejs.org/guide/deploy.html)。

---

Author：[@Yongchin](https://github.com/yongchin0821)
