import requests
import re
import json
import html
from openpyxl import Workbook

# =========================
# 🔑 填你的 Cookie 和 UA
# =========================
HEADERS = {
    "cookie": "YOUR_COOKIE",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36"
}

TOKEN = "YOUR_TOKEN"  # 改成你自己的

# =========================
# 🚀 开始抓取
# =========================
all_articles = []

for begin in range(0, 500, 10):  # 可改大一点
    print(f"正在抓取第 {begin} 条...")

    url = f"https://mp.weixin.qq.com/cgi-bin/appmsgpublish?sub=list&begin={begin}&count=10&token={TOKEN}&lang=zh_CN"

    res = requests.get(url, headers=HEADERS)
    text = res.text

    # 提取 JSON
    match = re.search(r'publish_page\s*=\s*(\{.*?\});', text, re.S)
    if not match:
        print("❌ 解析失败，可能 cookie 过期")
        break

    data = json.loads(match.group(1))

    publish_list = data.get("publish_list", [])
    if not publish_list:
        print("✅ 抓取完成")
        break

    for item in publish_list:
        raw = item["publish_info"]

        # 反转义
        decoded = html.unescape(raw)

        # 再解析
        info = json.loads(decoded)

        for msg in info["appmsg_info"]:
            all_articles.append({
                "title": msg["title"],
                "url": msg["content_url"],
                "read": msg.get("read_num", 0)
            })

print(f"\n总共抓到 {len(all_articles)} 篇文章")

# =========================
# 📊 导出 Excel
# =========================
wb = Workbook()
ws = wb.active
ws.title = "公众号文章"

# 表头
ws.append(["标题", "阅读量", "链接"])

# 数据
for a in all_articles:
    ws.append([a["title"], a["read"], a["url"]])

wb.save("wechat_articles.xlsx")

print("✅ 已导出：wechat_articles.xlsx")
