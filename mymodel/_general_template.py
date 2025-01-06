# 自定义模块说明
# 1. 将代码中所有<++>处替换为模块英文名称（注释中可用中文）
# 2. 填写模块的模板ID（在微信公众管理平台获得的）
# 3. send() 中修改<keyi> <valuei>
# 4. 如有需要，可增加一个get_infos() 函数用于中间处理report() 中的infos
# 调用说明
# 1. 导入自定义模块 import <++>
# 2. 根据模块的编写，定义好 infos 和 click_url
# 3. 调用模块以发送通知 <++>.report(infos, click_url)


# <++>模块
import json
import requests

# <++>模板ID
template_id = ""

# 配置
infos = ""
click_url = ""

def send(openId, infos, click_url, access_token):
    # touser 就是 openId
    # template_id 就是模板ID
    # click_url 就是点击模板跳转的url
    # data就按这种格式写，<key1>、<value1>就是{{<key1>.DATA}}中的那个<key1>，<value1>就是你要替换DATA的值
    body = {
        "touser": openId.strip(),
        "template_id": template_id.strip(),
        "url": click_url,
        "data": {
            "<key1>": {
                "value": "<value1>"
            },
            "<key2>": {
                "value": "<value2>"
            },
        }
    }
    url = 'https://api.weixin.qq.com/cgi-bin/message/template/send?access_token={}'.format(access_token)
    print('\t', end = '')
    print(requests.post(url, json.dumps(body)).text)


def report(openUsers: list, access_token: str, infos: str = infos, click_url: str = click_url):
    # 1. infos
    print(f"\n<++>： {infos}")
    # 2. 发送信息
    for openUser in openUsers:
        print(f"report <++> to {openUser['name']}")
        send(openUser["id"], infos, click_url, access_token)

