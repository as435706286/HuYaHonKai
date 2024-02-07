import time
import json
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import logging
import subprocess
from AllFunction import Login, DanMu, XingQiong, HeadLessLogin
from AllFunction import EveryDay

if __name__ == '__main__':
    logging.basicConfig(filename='HonKai_HuYa.log', level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    url = 'http://www.huya.com/29263932'
    driver = Login(url=url)
    # 点击开播领奖励
    # element = driver.find_element_by_xpath('//*[@id="matchComponent3"]/div/div[1]/div/div[2]')
    # driver.execute_script("arguments[0].click();", element)
    # time.sleep(1)
    # # 点击里程开播任务
    # element = driver.find_element_by_xpath('//*[@id="matchComponent12"]/diy/div/div[2]/div')
    # driver.execute_script("arguments[0].click();", element)
    # EveryDay()
    # DanMu()
    # XingQiong(driver)

