# 中国新闻模块
import json
import requests
import feedparser

# 中国新闻模板ID
template_id = "bLH7s5EYwgXtua2jRVXoCfd9hNURn2QLuXfn4Eujznw"

# 配置
rss_url = "https://www.chinanews.com.cn/rss/world.xml"
click_url = "https://www.chinanews.com.cn/world/"

def get_chinanews(rss_url):
    # 获取页面标题和第一条新闻信息
    feed = feedparser.parse(rss_url)
    entry0 = feed.entries[0]
    chinanews = {}
    chinanews["feedTitle"] = feed.feed.title
    chinanews["title"] = entry0.title
    chinanews["time"] = entry0.published
    chinanews["summary"] = entry0.get('summary', 'No summary available')
    return chinanews


def send(openId, chinanews, click_url, access_token):
    body = {
        "touser": openId.strip(),
        "template_id": template_id.strip(),
        "url": click_url,
        "data": {
            "feedTitle": {
                "value": chinanews["feedTitle"]
            },
            "title": {
                "value": chinanews["title"]
            },
            "time": {
                "value": chinanews["time"]
            },
            "summary": {
                "value": chinanews["summary"]
            },
        }
    }
    url = 'https://api.weixin.qq.com/cgi-bin/message/template/send?access_token={}'.format(access_token)
    print('\t', end = '')
    print(requests.post(url, json.dumps(body)).text)


def report(openUsers, access_token, rss_url = rss_url, click_url = click_url):
    # 1. 获取中国新闻
    chinanews = get_chinanews(rss_url)
    print(f"\n中国新闻： {chinanews}")
    # 2. 发送信息
    for openUser in openUsers:
        print(f"report chinanews to {openUser['name']}")
        send(openUser["id"], chinanews, click_url, access_token)
