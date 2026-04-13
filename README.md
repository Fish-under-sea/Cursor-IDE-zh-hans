

<p align="center">
  <strong>
    <span style="font-size: 2em; font-weight: 900;">
      汉&nbsp;&nbsp;化&nbsp;&nbsp;全&nbsp;&nbsp;适&nbsp;&nbsp;配
    </span>
  </strong>
  <br>
  <strong>
    <span style="font-size: 1.4em; color: #888; letter-spacing: 0.15em;">
      —— 强迫症福音 ——
    </span>
  </strong>
</p>

---

<p align="center">
  <img src="https://img.shields.io/badge/Cursor-IDE-brightgreen?style=for-the-badge&logo=cursor&logoColor=00E244" alt="Cursor">
  <img src="https://img.shields.io/badge/Language-Chinese%20Simplified-red?style=for-the-badge" alt="Chinese">
  <img src="https://img.shields.io/badge/VS%20Code%20Compat-100%25-blue?style=for-the-badge&logo=visual-studio-code&logoColor=007ACC" alt="VS Code Compatible">
  <img src="https://img.shields.io/badge/Translating-1982%2B%20Keys-gold?style=for-the-badge" alt="1982+ Keys Translated">
</p>

---

<p align="center">
  <strong style="font-size: 1.3em;">
    🔥 Cursor IDE 简体中文语言包 🔥
  </strong>
  <br>
  <strong>
    基于 Microsoft <a href="https://github.com/microsoft/vscode-loc">vscode-loc</a> 社区语言包开发
  </strong>
  <br>
  适配 Cursor 独家功能：Agent、Glass UI、Composer、Cursor Blame、MCP...
</p>

---

## 功能亮点

| 特性 | 说明 |
|------|------|
| **100% 兼容** | 基于 VS Code 语言包开发，VS Code 功能全部覆盖 |
| **Cursor 独家适配** | Agent 面板、Glass UI、Composer、Cursor Blame、MCP 工具等 Cursor 特有功能全翻译 |
| **1982+ 翻译条目** | 最新版本 1982 个缺失 key 已全部补全 |
| **持续跟进** | 随 Cursor 版本更新持续翻译新增内容 |
| **开箱即用** | 安装后重启 Cursor 或执行"配置显示语言"命令即可切换 |

## 安装方式

### 方式一：从 VSIX 安装（推荐）

1. 下载最新 `.vsix` 安装包
2. 在 Cursor 中运行"安装来自 VSIX 的扩展"命令
3. 选择下载的 `.vsix` 文件
4. 重启 Cursor

### 方式二：从源码构建

```bash
# 克隆本仓库
git clone https://github.com/YOUR_USERNAME/cursor-language-pack-zh-hans.git

# 安装依赖（需 Node.js）
npm install

# 打包为 VSIX
npm run package

# 安装
cursor --install-extension ./cursor-language-pack-zh-hans-*.vsix
```

### 方式三：本地链接安装（开发调试用）

```bash
# 在仓库目录下执行
npm install
npm run dev

# 然后在 Cursor 中启用此扩展
```

## 切换语言

1. 按 `Ctrl+Shift+P` 打开命令面板
2. 输入 `display` 搜索"配置显示语言"（Configure Display Language）
3. 选择 `中文(简体)`（Chinese (Simplified)）
4. 重启 Cursor

## 翻译覆盖范围

本语言包基于 Microsoft [vscode-loc](https://github.com/microsoft/vscode-loc) 社区翻译项目开发，在其基础上新增了大量 Cursor 独占功能的翻译。

### 已覆盖的模块类型

- **编辑器核心** — 编辑器选项、上下文键、内联补全、内联差异
- **Cursor Glass UI** — 代理面板、文件树、终端、边栏组件
- **Cursor Agent** — Agent 布局、代理操作、聊天操作
- **聊天功能** — Copilot 设置、聊天编辑、AI 配置、提示语法
- **Composer** — Composer 编辑器、浏览器组件
- **Cursor Blame** — Git Blame 集成、悬停视图
- **MCP 集成** — MCP 命令、配置、服务
- **扩展管理** — 扩展安装、监控、性能分析
- **终端** — Shell 集成、提示栏、补全配置
- **工作区** — 工作区配置、信任设置
- **窗口管理** — Electron 窗口操作、对话框
- **以及更多...**

### 翻译原则

- 准确性第一，确保翻译传达与原文完全相同的含义
- 简洁性优先，在准确的前提下使用简洁的中文表达
- 术语一致性，相同英文术语在不同位置保持统一翻译
- 占位符保护，`{N}`、`$(icon)`、`{key}` 格式的占位符原样保留
- 标点规范，中文使用全角标点符号
- 品牌词不翻译，Cursor、VS Code、Git、GitHub 等保持原样

## 开发说明

### 项目结构

```
cursor-language-pack-zh-hans/
├── translations/
│   ├── main.i18n.json              # 主语言包（核心翻译）
│   └── extensions/                  # 各扩展的语言包
├── .cursor/rules/                   # 翻译工作流规范
├── package.json                     # 扩展配置
└── README.cursor.md                 # 本文件
```

### 翻译工作流

每次 Cursor 版本更新后，通过分析脚本对比英文源文件与现有中文包，自动找出新增的缺失 key，补充翻译后合并回主文件。

## 致谢

本项目基于 **Microsoft [vscode-loc](https://github.com/microsoft/vscode-loc) 社区语言包** 开发。

vscode-loc 是微软官方的 VS Code 本地化开源项目，由全球社区志愿者共同维护。本项目的 VS Code 翻译部分直接来源于此，感谢所有参与 vscode-loc 翻译工作的贡献者。

特别感谢 [Joel Yang](https://github.com/jeasonstudio) 等早期贡献者，在项目向社区开放后翻译了大量新增字符串（4 万余字）。

---

<p align="center">

**尽情享用！愿天下再无英文界面！** 🎉

</p>
