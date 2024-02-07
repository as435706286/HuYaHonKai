import json
import requests

if __name__ == '__main__':
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36'
     }
    session = requests.session()
    # 加载本地cookies
    with open('cookies_huya.txt', 'r', encoding='utf8') as f:
        listCookies = json.loads(f.read())
    # 往session里添加cookies
        for cookie in listCookies:
            session.cookies.set(cookie['name'], cookie['value'])
    Qurl = "https://metric.huya.com/?ts=1700384077869"
    page_text = session.post(url=Qurl, headers=headers).text
    # data = json.loads(page_text)
    print(page_text)
