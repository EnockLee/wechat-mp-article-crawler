# WeChat MP Article Scraper

无需 API，抓取微信公众号后台文章列表，并导出标题、链接、阅读量到 Excel。

---

## ✨ 功能特点

- 📄 抓取公众号历史文章
- 🔗 提取文章链接（content_url）
- 📊 获取阅读量数据
- 📁 一键导出 Excel
- 🚫 无需官方 API

---

## 📦 安装依赖

```bash
pip install requests openpyxl
```

## 🚀 使用方法

### 1️⃣ 修改配置

在脚本中填写你的：

- Cookie  
- TOKEN  

示例：

```python
HEADERS = {
    "cookie": "你的cookie",
    "user-agent": "你的UA"
}

TOKEN = "你的token"
```

👉 获取方式：

- 打开微信公众号后台  
- 进入「内容与互动 → 草稿箱 / 已发表」  
- 按 F12 抓包即可获取  

---

### 2️⃣ 运行脚本

```bash
python wechat_mp.py
```

### 3️⃣ 输出结果

运行完成后，会生成：

```text
wechat_articles.xlsx
```

包含字段：

| 标题 | 阅读量 | 链接 |
|------|--------|------|

---

## ⚠️ 注意事项

- Cookie 会过期（一般 1~3 天）  
- TOKEN 每次登录会变化  

若出现解析失败：

```text
❌ 解析失败，可能 cookie 过期
```

请重新抓取 Cookie

## 📌 原理说明

通过模拟请求微信公众号后台接口：

/cgi-bin/appmsgpublish

解析返回页面中的：

publish_page JSON

提取文章数据。

## 🔧 后续可扩展

自动刷新 Cookie（Selenium）

CLI 命令行工具

Web UI 可视化界面

数据分析（爆款文章识别）

## ⭐ 如果对你有帮助

欢迎点个 Star 支持一下！

## 📄 License

MIT
