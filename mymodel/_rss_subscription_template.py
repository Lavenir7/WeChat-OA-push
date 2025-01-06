# <++>模块
import json
import requests
import feedparser

# <++>模板ID
template_id = ""

# 配置
rss_url = ""
click_url = ""

def get_<++>(rss_url):
    # 获取页面标题和第一条信息
    feed = feedparser.parse(rss_url)
    entry0 = feed.entries[0]
    news = {}
    news["feedTitle"] = feed.feed.title
    news["title"] = entry0.title
    news["time"] = entry0.published
    news["summary"] = entry0.get('summary', 'No summary available')
    return news


def send(openId, news, click_url, access_token):
    body = {
        "touser": openId.strip(),
        "template_id": template_id.strip(),
        "url": click_url,
        "data": {
            "feedTitle": {
                "value": news["feedTitle"]
            },
            "title": {
                "value": news["title"]
            },
            "time": {
                "value": news["time"]
            },
            "summary": {
                "value": news["summary"]
            },
        }
    }
    url = 'https://api.weixin.qq.com/cgi-bin/message/template/send?access_token={}'.format(access_token)
    print('\t', end = '')
    print(requests.post(url, json.dumps(body)).text)


def report(openUsers, access_token, rss_url = rss_url, click_url = click_url):
    # 1. 获取信息
    news = get_<++>(rss_url)
    print(f"\n<++>： {news}")
    # 2. 发送信息
    for openUser in openUsers:
        print(f"report news to {openUser['name']}")
        send(openUser["id"], news, click_url, access_token)
