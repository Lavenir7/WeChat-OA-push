import json
import requests

class global_infos:
    def __init__(self, infos_json: str):
        infos_json = "./secrets.json"
        with open(infos_json) as f:
            infos = json.loads(f.read())

        # 测试号信息
        self.appID = infos["appInfos"]["appID"]
        self.appSecret = infos["appInfos"]["appSecret"]

        # 收信人信息
        self.userInfos = []
        for useri in infos["userInfos"]:
            self.userInfos.append(infos["userInfos"][useri])

        # token 获取
        self.access_token = "can't get access_token"
        self.get_access_token()

    def get_access_token(self):
        # 获取access token的url
        url = 'https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid={}&secret={}' \
            .format(self.appID.strip(), self.appSecret.strip())
        response = requests.get(url).json()
        # print(response)
        self.access_token = response.get('access_token')

    def get_openUsers(self, openList):
        # 获取发送用户列表
        openUsers = [self.userInfos[openIndex] for openIndex, openi in enumerate(openList) if openi]
        return openUsers
