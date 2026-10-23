# NAIM Holdings 房产管理与 AI 系统

[English](README.md)

本项目是 COS20031 Individual Assessment 使用的一个小型 Flask 网页应用。系统以 NAIM Holdings 为主题，提供简单的房产资料管理功能，并连接 Google Gemini API 来回答用户问题。

## 主要功能

- 从首页打开 NAIM Holdings 官方网站。
- 新增房产资料，包括 ID、名称、描述和价格。
- 显示数据库中储存的房产资料。
- 根据房产 ID 搜索房产。
- 将问题发送给 Gemini，并显示 AI 生成的回答。
- 使用本地 SQLite 数据库存储房产记录。

当前版本是一个教学原型。虽然 assessment 文件讨论了 Retrieval-Augmented Generation（RAG），但目前的程式会直接把用户问题发送给 Gemini，并没有实现文件知识库检索、向量数据库或完整的 RAG pipeline。

## 使用的技术

- Python
- Flask
- SQLite
- Google Gemini API
- HTML 和 CSS
- Jinja templates

## 环境要求

- 已安装 Python，并且可以在终端执行
- Google Gemini API key
- 使用 Gemini 问答时需要互联网连接

程式使用的依赖套件如下：

```text
Flask
python-dotenv
google-generativeai
```

## 安装与部署

### 1. 打开项目

在终端进入项目根目录，也就是包含 `app.py` 的目录。

### 2. 建立虚拟环境

Windows PowerShell：

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

Windows Command Prompt：

```bat
python -m venv .venv
.venv\Scripts\activate
```

macOS 或 Linux：

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. 安装依赖套件

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

目前 `requirements.txt` 是空的，因此需要手动安装以上套件，除非之后补充依赖文件。

### 4. 设置 Gemini API key

将 `.env.examples` 复制成名为 `.env` 的文件：

Windows PowerShell：

```powershell
Copy-Item .env.examples .env
```

macOS 或 Linux：

```bash
cp .env.examples .env
```

打开 `.env`，把占位值替换成真实的 API key：

```env
GEMINI_API_KEY=your_gemini_api_key
```

不要提交或分享 `.env` 和 API key。`.gitignore` 已经设置为忽略 `.env`。

### 5. 启动系统

请在项目根目录执行：

```bash
python app.py
```

启动后可以通过 <http://127.0.0.1:5000> 访问系统。

## 系统使用方法

### 首页

首页提供 NAIM Holdings 官方网站、新增房产、搜索房产和 Gemini AI 问答的入口。

### 新增房产

1. 打开 **Add New Real Estate**。
2. 输入房产 ID、名称、描述和价格。
3. 点击 **Create**。

房产 ID 必须唯一，因为它是数据库的主键。

### 搜索房产

1. 打开 **Real Estate Search**。
2. 输入房产 ID。
3. 点击 **Search**。

如果直接打开搜索页面，当前程式会显示数据库中的所有房产记录。

### 使用 Gemini AI

1. 打开 **Ask for Gemini AI**。
2. 输入问题。
3. 提交表单。

使用这个功能需要互联网连接和有效的 API key。

## 项目目录结构

```text
COS20031-Individual-Assignment/
├── app.py                         # Flask 应用程式和路由
├── database/
│   └── estate.db                  # SQLite 数据库文件
├── src/
│   ├── estate.py                  # 数据库操作
│   └── gemini.py                  # Gemini API 整合
├── static/
│   ├── styles.css                 # 网页样式
│   └── icon.ico                   # 网页图标
├── template/
│   ├── index.html                 # 首页
│   ├── add_estate.html             # 新增房产页面
│   ├── search.html                 # 搜索结果页面
│   └── ask.html                    # Gemini 问答页面
├── .env.examples                  # 环境变量示例
├── .gitignore                     # 忽略文件和密钥
├── requirements.txt               # 依赖文件，目前为空
├── README.md                      # 英文说明文件
└── README.zh-CN.md                # 简体中文说明文件
```

## 重要开发说明

- 直接运行 `app.py` 时，程式会调用 `create_estate()`，删除并重新建立 `Estate_Table`，然后加入三笔示范资料。因此重新启动时可能会删除现有房产资料。
- 当前程式开启了 Flask debug mode，只适合本地开发，不适合直接用于正式部署。
- 数据库使用相对路径，所以应该从项目根目录启动程式。
- 当前原型没有用户登入、CSRF 防护和完整的生产环境输入验证。
- Gemini API 错误和不合法的数据库输入目前没有完整处理。

## Assessment 背景

assessment 文件说明了 RAG 可以如何帮助房地产资料检索、客户服务、决策支持和项目管理。当前实现展示了网页界面、SQLite 房产管理和 Gemini 问答功能，为之后扩展成完整的 RAG 系统提供基础。
