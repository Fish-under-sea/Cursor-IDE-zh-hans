> **⏸️ 暂停维护** · 最近提交：2026-04-14（约 5 个月前）
>
> 汉化词条依赖上游 Microsoft vscode-loc 词库；等上游词条更新后同步跟进。

<div align="center">

# 🔥 Cursor IDE 简体中文语言包 🔥

**汉化全适配 —— 强迫症福音**

基于 Microsoft [`vscode-loc`](https://github.com/microsoft/vscode-loc) 社区语言包开发 · 适配 Cursor 独家功能

![Cursor](https://img.shields.io/badge/Cursor-IDE-brightgreen?style=flat-square) ![Language](https://img.shields.io/badge/Language-简体中文-red?style=flat-square) ![VS Code Compat](https://img.shields.io/badge/VS%20Code%20Compat-100%25-blue?style=flat-square) ![Entries](https://img.shields.io/badge/翻译条目-1982%2B-gold?style=flat-square)

</div>

---

## ✨ 功能亮点

| 特性 | 说明 |
|------|------|
| **100% 兼容** | 基于 VS Code 语言包开发，VS Code 功能全部覆盖 |
| **Cursor 独家适配** | Agent 面板、Glass UI、Composer、Cursor Blame、MCP 工具等 Cursor 特有功能全翻译 |
| **1982+ 翻译条目** | 最新版本 1982 个缺失 key 已全部补全 |
| **持续跟进** | 随 Cursor 版本更新持续翻译新增内容 |
| **开箱即用** | 安装后重启 Cursor 或执行「配置显示语言」命令即可切换 |

## 📦 安装方式

### 方式一：从 VSIX 安装（推荐）

下载仓库中的 `.vsix` 文件，然后在 Cursor 中：

```bash
# 命令面板（Ctrl+Shift+P）→ 输入：
Extensions: Install from VSIX...
```

> 若仓库未附带 `.vsix`，请用方式二自行构建。

### 方式二：从源码构建

```bash
# 克隆本仓库
git clone https://github.com/Fish-under-sea/Cursor-IDE-zh-hans.git
cd Cursor-IDE-zh-hans

# 安装依赖（需 Node.js）
npm install

# 打包为 VSIX
npx vsce package

# 安装
# 命令面板 → Extensions: Install from VSIX... → 选择生成的 .vsix
```

### 方式三：本地链接安装（开发调试用）

```bash
# 在仓库目录下执行
# 将本目录链接到 Cursor 扩展目录，改动即时生效
```

### 切换语言

安装完成后：

1. **重启 Cursor**，或
2. 打开命令面板（`Ctrl+Shift+P`），执行 `Configure Display Language` → 选择 **中文（简体）**

## 🌐 翻译覆盖范围

本语言包基于 Microsoft [`vscode-loc`](https://github.com/microsoft/vscode-loc) 社区翻译项目开发，在其基础上**新增了大量 Cursor 独占功能的翻译**。

### 已覆盖的模块类型

| 模块 | 覆盖内容 |
|------|---------|
| **编辑器核心** | 编辑器选项、上下文键、内联补全、内联差异 |
| **Cursor Glass UI** | 代理面板、文件树、终端、边栏组件 |
| **Cursor Agent** | Agent 布局、代理操作、聊天操作 |
| **聊天功能** | Copilot 设置、聊天编辑、AI 配置、提示语法 |
| **Composer** | Composer 编辑器、浏览器组件 |
| **Cursor Blame** | Git Blame 集成、悬停视图 |
| **MCP 集成** | MCP 命令、配置、服务 |
| **扩展管理** | 扩展安装、监控、性能分析 |
| **终端** | Shell 集成、提示栏、补全配置 |
| **工作区** | 工作区配置、信任设置 |
| **窗口管理** | Electron 窗口操作、对话框 |

### 翻译原则

| 原则 | 含义 |
|------|------|
| **准确性第一** | 确保翻译传达与原文**完全相同**的含义 |
| **简洁性优先** | 在准确的前提下使用简洁的中文表达 |
| **术语一致性** | 相同英文术语在不同位置保持统一翻译 |
| **占位符保护** | `{N}`、`$(icon)`、`{key}` 格式的占位符**原样保留** |
| **标点规范** | 中文使用全角标点符号 |
| **品牌词不翻译** | Cursor、VS Code、Git、GitHub 等保持原样 |

## 🔧 硬编码字符串修复脚本

Cursor 部分功能（如「将符号添加到聊天」菜单项）的字符串**硬编码在源码中**，不经过 i18n 系统，因此语言包无法翻译这些内容。

为此提供了 `cursor_menu_translate.py`，直接修改 Cursor 编译后的 JS 文件：

```bash
# 运行脚本（需要管理员权限）
python cursor_menu_translate.py
```

**功能说明**：

- `Add Symbol to Current Chat...` → `将符号添加到当前聊天...`
- `Add Symbol to New Chat...` → `将符号添加到新聊天...`

> ⚠️ **注意**：
> - **每次 Cursor 更新后需要重新运行**此脚本
> - **需要以管理员身份运行**（会写入 Cursor 安装目录）

## 🛠️ 技术栈与项目信息

| 项 | 内容 |
|----|------|
| 扩展名 | `cursor-language-pack-zh-hans` |
| 显示名 | Chinese (Simplified) (简体中文) Language Pack for cursor |
| 版本 | **1.111.2** |
| 发布者 | `Fish-under-sea` |
| 语言包文件 | `translations/main.i18n.json` + `translations/extensions/`（92 个扩展语言包） |
| 运行脚本 | `npm run update` |
| 最小 VS Code 版本 | `^1.0.0` |

## 📁 项目结构

```text
cursor-language-pack-zh-hans/
├── translations/
│   ├── main.i18n.json              # 主语言包（核心翻译）
│   └── extensions/                 # 各扩展的语言包（92 个）
├── cursor_menu_translate.py        # 硬编码字符串汉化脚本
├── package.json                    # 扩展配置
├── README.vscode.md                # VS Code 部分说明
├── CHANGELOG.md                    # 变更日志
├── languagepack.png                # 图标
└── .vscodeignore
```

## 🔄 翻译工作流

每次 Cursor 版本更新后，通过分析脚本**对比英文源文件与现有中文包**，自动找出新增的缺失 key，补充翻译后合并回主文件。

## 🙏 致谢

本项目基于 **Microsoft [`vscode-loc`](https://github.com/microsoft/vscode-loc) 社区语言包** 开发。

`vscode-loc` 是微软官方的 VS Code 本地化开源项目，由全球社区志愿者共同维护。本项目的 VS Code 翻译部分直接来源于此 —— **感谢所有参与 vscode-loc 翻译工作的贡献者**。

特别感谢 [Joel Yang](https://github.com/jeasonstudio) 等早期贡献者，在项目向社区开放后翻译了大量新增字符串（4 万余字）。

## ⚠️ 已知情况

| 项 | 说明 |
|----|------|
| **许可** | 已添加 **MIT LICENSE**（根目录 `LICENSE`）。`package.json` 中仍写作「SEE MIT LICENSE IN LICENSE.md」，指向的文件名与实际不符，可按需改为 `LICENSE` |
| **文档中的两处路径不存在** | 原有说明的项目结构里列出 `README.cursor.md` 与 `.cursor/rules/`，实测分别是 `README.vscode.md` 与**不存在**（本 README 已按实测修正） |

---

<p align="center">

**尽情享用！愿天下再无英文界面！** 🎉

</p>