# 微信 | 公众平台
# https://mp.weixin.qq.com/debug/cgi-bin/sandbox?t=sandbox/login

from global_infos import *
# 导入自定义模块库
from mymodel import weather_today # 天气预报
from mymodel import schedule_today # 日程表
from mymodel import chinanews_today # 中国新闻

import time
import schedule

if __name__ == '__main__':
    infos_json = "secrets.json"
    ginfos = global_infos(infos_json)
    openAll = [True] * len(ginfos.userInfos)
    daily_times = ("07:00", "09:00", "12:00", "18:00")

    # 天气预报
    for daily_time in daily_times:
        schedule.every().day.at(daily_time).do(weather_today.report, ginfos.get_openUsers(openAll), ginfos.access_token)
    
    # 日程表
    for daily_time in daily_times:
        schedule.every().day.at(daily_time).do(schedule_today.report, ginfos.get_openUsers([1, 0]), ginfos.access_token)

    # 中国新闻
    for daily_time in daily_times:
        schedule.every().day.at(daily_time).do(chinanews_today.report, ginfos.get_openUsers(openAll), ginfos.access_token)

    while True:
        schedule.run_pending()
        time.sleep(1)
