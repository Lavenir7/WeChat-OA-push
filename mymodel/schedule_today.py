# 日程表模块
import json
import requests

# 时间表模板ID
template_id = "UIGgq3vXZMBZ5AuTYOAQGG_xphUZk7pp4ZRhnmjcuXk"

# 配置
schedules = "1. 学习《深度学习》； 2. 书店退卡，100押金。"
click_url = "https://sharedchat.fun/"

def send(openId, schedules, click_url, access_token):
    body = {
        "touser": openId,
        "template_id": template_id.strip(),
        "url": click_url,
        "data": {
            "message": {
                "value": schedules
            },
        }
    }
    url = 'https://api.weixin.qq.com/cgi-bin/message/template/send?access_token={}'.format(access_token)
    print('\t', end = '')
    print(requests.post(url, json.dumps(body)).text)


def report(openUsers, access_token, schedules = schedules, click_url = click_url):
    # 1. 打印日程信息
    print(f"\n日程信息：{schedules}")
    # 2. 发送信息
    for openUser in openUsers:
        print(f"report schedule to {openUser['name']}")
        send(openUser["id"], schedules, click_url, access_token)
