import time
import json
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.binary_location = "../Chrome/chrome.exe"
driver = webdriver.Chrome("../Chrome/chromedriver.exe", options=options)

# ---------------------获取cookies
# 打开主页
driver.get('http://www.huya.com/29263932')
time.sleep(15)
dictCookies = driver.get_cookies()
jsonCookies = json.dumps(dictCookies)
print(dictCookies)
with open('./cookies_huya.txt', 'w') as f:
    f.write(jsonCookies)
print('cookies保存成功！')
driver.quit()
