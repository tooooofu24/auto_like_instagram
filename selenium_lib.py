from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import platform
import requests
from const import INSTAGRAM_API_BASE_URL
from const import INSTAGRAM_API_URL_PARAMETER


def setup():
    # lambdaで起動したときの処理
    if platform.system() == 'Linux':
        print('lambdaで起動します')
        # ブラウザ(Chrome)の設定
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")
        options.add_argument("--window-size=1080x1280")
        options.add_argument("--disable-gpu")
        options.add_argument("--disable-application-cache")
        options.add_argument("--disable-infobars")
        options.add_argument("--no-sandbox")
        options.add_argument("--hide-scrollbars")
        options.add_argument("--enable-logging")
        options.add_argument("--log-level=0")
        options.add_argument("--single-process")
        options.add_argument("--ignore-certificate-errors")
        options.add_argument("--homedir=/tmp")
        options.add_argument(
            '--user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1 Safari/605.1.15')
        options.binary_location = "/opt/python/bin/headless-chromium"

        # ブラウザの定義
        driver = webdriver.Chrome(
            "/opt/python/bin/chromedriver",
            chrome_options=options
        )
    # local(mac)で起動したとき
    else:
        print('ローカルで起動します')
        s = Service('/Users/kawakamiriko/Downloads/chromedriver')
        options = webdriver.ChromeOptions()
        # options.add_argument("--headless")
        options.add_argument("--window-size=1080x1280")
        driver = webdriver.Chrome(service=s, options=options)

    return driver


def getUrls(tag_id) -> list:
    urls = []
    r = requests.get(INSTAGRAM_API_BASE_URL + tag_id +
                     INSTAGRAM_API_URL_PARAMETER)
    posts = r.json()['data']
    for post in posts:
        url = post['permalink']
        urls.append(url)
    return urls
