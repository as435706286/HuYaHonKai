import time
import json

import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import logging
import subprocess

url = 'http://www.huya.com/29263932'


def Login(url):
    options = Options()
    options.binary_location = "../Chrome/chrome.exe"
    driver = webdriver.Chrome("../Chrome/chromedriver.exe", options=options)
    # 打开主页
    driver.get(url=url)
    driver.implicitly_wait(5)
    # 加载本地cookies
    with open('cookies_huya.txt', 'r', encoding='utf8') as f:
        listCookies = json.loads(f.read())
    # 往driver里添加cookies
        for cookie in listCookies:
            if 'expiry' in cookie:  # 有的cookie里面有这个参数，有的没有。有的话，需要做处理。
                del cookie['expiry']  # 这个expiry参数值得类型会影响到登录识别，所以需要删掉或者更改值为整形
                driver.add_cookie(cookie)
    # 刷新页面
    driver.refresh()
    time.sleep(2)
    # 模拟鼠标滚轮，滑动至页面底部
    js = "window.scrollTo(0, document.body.scrollHeight)"
    driver.execute_script(js)
    logging.info("登录成功！")
    return driver


def HeadLessLogin(url):
    options = Options()
    prefs = {"profile.managed_default_content_settings.images": 2}
    options.add_experimental_option("prefs", prefs)
    options.binary_location = "../Chrome/chrome.exe"
    options.add_argument('--headless')
    driver = webdriver.Chrome("../Chrome/chromedriver.exe", options=options)
    # 打开主页
    driver.get(url=url)
    driver.implicitly_wait(5)
    # 加载本地cookies
    with open('cookies_huya.txt', 'r', encoding='utf8') as f:
        listCookies = json.loads(f.read())
        # 往driver里添加cookies
        for cookie in listCookies:
            driver.add_cookie(cookie)
    # 刷新页面
    driver.refresh()
    time.sleep(2)
    # 模拟鼠标滚轮，滑动至页面底部
    js = "window.scrollTo(0,document.body.scrollHeight)"
    driver.execute_script(js)
    logging.info("HeadLess登录成功！")
    return driver


# -----------------------领取每日开播任务奖励
def EveryDay():
    driver = HeadLessLogin(url=url)
    time.sleep(5)
    try:
        # 模拟鼠标滚轮，滑动至页面底部
        js = "window.scrollTo(0,document.body.scrollHeight)"
        driver.execute_script(js)
        # driver.execute_script('window.scrollBy(0,500)')
        time.sleep(1)
        # 点击开播领奖励
        element = driver.find_element_by_xpath('//*[@id="matchComponent3"]/div/div[1]/div/div[2]')
        driver.execute_script("arguments[0].click();", element)
        time.sleep(1)
        # 点击里程开播任务
        element = driver.find_element_by_xpath('//*[@id="matchComponent12"]/diy/div/div[2]/div')
        driver.execute_script("arguments[0].click();", element)
        time.sleep(1)
        # 领取
        element = driver.find_element_by_xpath('//*[@id="matchComponent24"]/div/div[1]/div[2]/div/div/ul/li[6]/button')
        driver.execute_script("arguments[0].click();", element)
        time.sleep(1)
        element = driver.find_element_by_xpath('//*[@id="matchComponent24"]/div/div[1]/div[2]/div/div/ul/li[5]/button')
        driver.execute_script("arguments[0].click();", element)
        time.sleep(1)
        element = driver.find_element_by_xpath('//*[@id="matchComponent24"]/div/div[1]/div[2]/div/div/ul/li[4]/button')
        driver.execute_script("arguments[0].click();", element)
        time.sleep(1)
        element = driver.find_element_by_xpath('//*[@id="matchComponent24"]/div/div[1]/div[2]/div/div/ul/li[3]/button')
        driver.execute_script("arguments[0].click();", element)
        time.sleep(1)
        element = driver.find_element_by_xpath('//*[@id="matchComponent24"]/div/div[1]/div[2]/div/div/ul/li[2]/button')
        driver.execute_script("arguments[0].click();", element)
        time.sleep(1)
        element = driver.find_element_by_xpath('//*[@id="matchComponent24"]/div/div[1]/div[2]/div/div/ul/li[1]/button')
        driver.execute_script("arguments[0].click();", element)
        time.sleep(1)
        logging.info("领取每日开播任务奖励成功！")
        # 领取1
        element = driver.find_element_by_xpath('//*[@id="matchComponent24"]/div/div[1]/div[1]/div/div[2]/div[3]/div[2]/div[1]/ul/li[1]/p/button')
        driver.execute_script("arguments[0].click();",element)
        time.sleep(1)
        # 领取2
        element = driver.find_element_by_xpath('//*[@id="matchComponent24"]/div/div[1]/div[1]/div/div[2]/div[3]/div[2]/div[1]/ul/li[2]/p/button')
        driver.execute_script("arguments[0].click();",element)
        time.sleep(1)
        # 领取3
        element = driver.find_element_by_xpath('//*[@id="matchComponent24"]/div/div[1]/div[1]/div/div[2]/div[3]/div[2]/div[1]/ul/li[3]/p/button')
        driver.execute_script("arguments[0].click();",element)
        time.sleep(1)
        # 领取4
        element = driver.find_element_by_xpath('//*[@id="matchComponent24"]/div/div[1]/div[1]/div/div[2]/div[3]/div[2]/div[1]/ul/li[4]/p/button')
        driver.execute_script("arguments[0].click();",element)
        time.sleep(1)
        logging.info("领取直播星琼成功！")
        driver.quit()
    except:
        logging.error("领取直播星琼失败！")
        driver.quit()


# -----------------------领取直播星琼
def XingQiong(driver):
    # 刷新
    driver.refresh()
    # 点击开播领奖励
    element = driver.find_element_by_xpath('//*[@id="matchComponent3"]/div/div[1]/div/div[2]')
    driver.execute_script("arguments[0].click();", element)
    time.sleep(1)
    # 点击里程开播任务
    element = driver.find_element_by_xpath('//*[@id="matchComponent12"]/diy/div/div[2]/div')
    driver.execute_script("arguments[0].click();",element)
    time.sleep(1)
    # 领取1
    element = driver.find_element_by_xpath('//*[@id="matchComponent19"]/div/div[1]/div[1]/div/div[2]/div[3]/div[2]/div[1]/ul/li[1]/p/button')
    driver.execute_script("arguments[0].click();",element)
    time.sleep(1)
    # 领取2
    element = driver.find_element_by_xpath('//*[@id="matchComponent19"]/div/div[1]/div[1]/div/div[2]/div[3]/div[2]/div[1]/ul/li[2]/p/button')
    driver.execute_script("arguments[0].click();",element)
    time.sleep(1)
    # 领取3
    element = driver.find_element_by_xpath('//*[@id="matchComponent19"]/div/div[1]/div[1]/div/div[2]/div[3]/div[2]/div[1]/ul/li[3]/p/button')
    driver.execute_script("arguments[0].click();",element)
    time.sleep(1)
    # 领取4
    element = driver.find_element_by_xpath('//*[@id="matchComponent19"]/div/div[1]/div[1]/div/div[2]/div[3]/div[2]/div[1]/ul/li[4]/p/button')
    driver.execute_script("arguments[0].click();",element)
    time.sleep(1)
    logging.info("领取直播星琼成功！")


# -----------------------领取每日开播任务2奖励(开播1小时)
def EveryDay2(driver):
    # 点击开播领奖励
    element = driver.find_element_by_xpath('//*[@id="matchComponent3"]/div/div[1]/div/div[2]')
    driver.execute_script("arguments[0].click();", element)
    time.sleep(1)
    # 点击里程开播任务
    element = driver.find_element_by_xpath('//*[@id="matchComponent10"]/diy/div/div[2]/div')
    driver.execute_script("arguments[0].click();",element)
    time.sleep(1)
    element = driver.find_element_by_xpath('//*[@id="matchComponent20"]/div/div[1]/div[2]/div/div/ul/li[4]/button')
    driver.execute_script("arguments[0].click();",element)
    time.sleep(1)
    logging.info("领取每日开播任务3奖励成功！")


# -----------------------领取每日开播任务4奖励
def EveryDay4(driver):
    # 点击开播福利
    element = driver.find_element_by_xpath('//*[@id="bc57"]')
    driver.execute_script("arguments[0].click();", element)
    time.sleep(1)
    element = driver.find_element_by_xpath('//*[@id="bc3398"]/div/button')
    driver.execute_script("arguments[0].click();",element)
    time.sleep(1)
    logging.info("领取每日开播任务4奖励成功！")


# -----------------------关机
def ShutDown():
    # 执行关机命令
    shutdown_command = "shutdown /s /t 0"
    subprocess.call(shutdown_command, shell=True)


# -----------------------获取cookies
def GetCookies():
    # 打开主页
    options = Options()
    options.binary_location = "../Chrome/chrome.exe"
    driver = webdriver.Chrome("../Chrome/chromedriver.exe", options=options)
    driver.get('www.huya.com')
    driver.implicitly_wait(5)
    # 点击登录
    element = driver.find_element_by_xpath('//*[@id="js-header"]/div/div[1]/div[3]/div[7]/div')
    element.click()
    session = requests.session()
    while True:
        dictCookies = driver.get_cookies()
        # 往session里添加cookies
        for cookie in dictCookies:
            session.cookies.set(cookie['name'], cookie['value'])
        param = {
            'actAlias': actAlias
        }
        url = 'https://www.douyu.com/japi/carnival/nc/giftbag/myrecord?'
        page_text = session.get(url=url, headers=headers, params=param).text
        data = json.loads(page_text)
        if data["msg"] == "操作成功":
            jsonCookies = json.dumps(dictCookies)
            print(dictCookies)
            with open('cookies_huya.txt', 'w') as f:
                f.write(jsonCookies)
            logging.info('cookies保存成功！')
            driver.quit()
            break


# -----------------------发弹幕
def DanMu():
    driver = HeadLessLogin(url=url)
    time.sleep(5)
    try:
        driver.refresh()
        time.sleep(1)
        element1 = driver.find_element_by_xpath('//*[@id="pub_msg_input"]')
        element1.send_keys('1')
        time.sleep(1)
        element = driver.find_element_by_xpath('//*[@id="msg_send_bt"]')
        driver.execute_script("arguments[0].click();",element)
        time.sleep(1)
        element1.send_keys('2')
        time.sleep(1)
        driver.execute_script("arguments[0].click();",element)
        time.sleep(1)
        element1.send_keys('3')
        time.sleep(1)
        driver.execute_script("arguments[0].click();",element)
        time.sleep(1)
        element1 = driver.find_element_by_xpath('//*[@id="pub_msg_input"]')
        element = driver.find_element_by_xpath('//*[@id="msg_send_bt"]')
        element1.send_keys('4')
        time.sleep(1)
        driver.execute_script("arguments[0].click();",element)
        time.sleep(1)
        element1.send_keys('5')
        time.sleep(1)
        driver.execute_script("arguments[0].click();",element)
        time.sleep(1)
        logging.info("发送弹幕成功！")
        driver.quit()
    except:
        logging.error("领取直播星琼失败！")
        driver.quit()


