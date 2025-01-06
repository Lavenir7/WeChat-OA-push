# 天气预报模块
import json
import requests
from bs4 import BeautifulSoup

# 天气预报模板ID
template_id = "6CeY6G2OrRFCtqKRkxT0wZBPOTefZv0xgyp0cG7_t3Y"

# 配置
city = "滨州"
click_url = "https://www.weather.com.cn/weather1d/101121101.shtml#search" # 滨州

def get_weather(my_city):
    urls = ["http://www.weather.com.cn/textFC/hb.shtml",
            "http://www.weather.com.cn/textFC/db.shtml",
            "http://www.weather.com.cn/textFC/hd.shtml",
            "http://www.weather.com.cn/textFC/hz.shtml",
            "http://www.weather.com.cn/textFC/hn.shtml",
            "http://www.weather.com.cn/textFC/xb.shtml",
            "http://www.weather.com.cn/textFC/xn.shtml"
            ]
    for url in urls:
        resp = requests.get(url)
        text = resp.content.decode("utf-8")
        soup = BeautifulSoup(text, 'html5lib')
        div_conMidtab = soup.find("div", class_="conMidtab")
        tables = div_conMidtab.find_all("table")
        for table in tables:
            trs = table.find_all("tr")[2:]
            for index, tr in enumerate(trs):
                tds = tr.find_all("td")
                # 这里倒着数，因为每个省会的td结构跟其他不一样
                city_td = tds[-8]
                this_city = list(city_td.stripped_strings)[0]
                if this_city == my_city:

                    high_temp_td = tds[-5]
                    low_temp_td = tds[-2]
                    weather_type_day_td = tds[-7]
                    weather_type_night_td = tds[-4]
                    wind_td_day = tds[-6]
                    wind_td_day_night = tds[-3]

                    high_temp = list(high_temp_td.stripped_strings)[0]
                    low_temp = list(low_temp_td.stripped_strings)[0]
                    weather_typ_day = list(weather_type_day_td.stripped_strings)[0]
                    weather_type_night = list(weather_type_night_td.stripped_strings)[0]

                    wind_day = list(wind_td_day.stripped_strings)[0] + list(wind_td_day.stripped_strings)[1]
                    wind_night = list(wind_td_day_night.stripped_strings)[0] + list(wind_td_day_night.stripped_strings)[1]

                    # 如果没有白天的数据就使用夜间的
                    temp = f"{low_temp}——{high_temp}摄氏度" if high_temp != "-" else f"{low_temp}摄氏度"
                    weather_typ = weather_typ_day if weather_typ_day != "-" else weather_type_night
                    wind = f"{wind_day}" if wind_day != "--" else f"{wind_night}"
                    return this_city, temp, weather_typ, wind


def get_daily_love():
    # 每日一句情话
    url = "https://api.lovelive.tools/api/SweetNothings/Serialization/Json"
    r = requests.get(url)
    all_dict = json.loads(r.text)
    sentence = all_dict['returnObj'][0]
    daily_love = sentence
    return daily_love


def send(openId, weather, click_url, access_token):
    import datetime
    today = datetime.date.today()
    today_str = today.strftime("%Y年%m月%d日")

    body = {
        "touser": openId.strip(),
        "template_id": template_id.strip(),
        "url": click_url,
        "data": {
            "date": {
                "value": today_str
            },
            "region": {
                "value": weather[0]
            },
            "weather": {
                "value": weather[2]
            },
            "temp": {
                "value": weather[1]
            },
            "wind_dir": {
                "value": weather[3]
            },
            "today_note": {
                # "value": get_daily_love()
                "value": "这是一条备注"
            }
        }
    }
    url = 'https://api.weixin.qq.com/cgi-bin/message/template/send?access_token={}'.format(access_token)
    print('\t', end = '')
    print(requests.post(url, json.dumps(body)).text)


def report(openUsers, access_token, city = city, click_url = click_url):
    # 1. 获取天气
    weather = get_weather(city)
    print(f"\n天气信息：{weather}")
    # 2. 发送信息
    for openUser in openUsers:
        print(f"report weather to {openUser['name']}")
        send(openUser["id"], weather, click_url, access_token)
