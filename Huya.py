from AllFunction import Login, XingQiong, HeadLessLogin
from AllFunction import EveryDay
from AllFunction import DanMu
from AllFunction import ShutDown
import schedule
import logging

if __name__ == '__main__':
    logging.basicConfig(filename='HonKai_HuYa.log', level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    url = 'http://www.huya.com/29263932'
    driver = HeadLessLogin(url=url)
    # 每天0:00执行发弹幕
    schedule.every().day.at("00:00").do(DanMu)
    # 每天0:02执行发弹幕
    schedule.every().day.at("00:02").do(DanMu)
    # 每天0:03执行抢
    schedule.every().day.at("00:03").do(EveryDay)
    # 每天0:04执行抢
    schedule.every().day.at("00:04").do(EveryDay)
    # 每天0:05执行抢
    schedule.every().day.at("00:05").do(EveryDay)
    #  每天0:11执行抢
    schedule.every().day.at("00:11").do(EveryDay)
    #  每天0:12执行抢
    schedule.every().day.at("00:12").do(EveryDay)
    #  每天0:13执行抢
    schedule.every().day.at("00:13").do(EveryDay)
    # 每天1:00执行抢
    schedule.every().day.at("01:00").do(EveryDay)
    # 每天1:01执行抢
    schedule.every().day.at("01:01").do(EveryDay)
    # 每天1:02执行抢
    schedule.every().day.at("01:02").do(EveryDay)
    # 每天1:03执行抢
    schedule.every().day.at("01:03").do(EveryDay)
    # 每天2:00执行
    schedule.every().day.at("02:00").do(EveryDay)
    # 每天2:01执行
    schedule.every().day.at("02:01").do(EveryDay)
    # 每天2:02执行
    schedule.every().day.at("02:02").do(EveryDay)
    # 每天2:03执行
    schedule.every().day.at("02:03").do(EveryDay)
    # 每天2:10执行
    schedule.every().day.at("02:10").do(EveryDay)
    while True:
        schedule.run_pending()
