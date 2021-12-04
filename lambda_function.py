import json
import requests
import time
import traceback
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as ECpython
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
import instagram
from const import INSTAGRAM_API_URL


def lambda_handler(event, context):

    urls = []
    r = requests.get(INSTAGRAM_API_URL)
    posts = r.json()['data']
    print(posts)
    print(str(len(posts))+'件の投稿にいいねします')
    for post in posts:
        url = post['permalink']
        urls.append(url)

    print(urls)

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

    print('ログインします')
    instagram.login(driver)
    time.sleep(5)
    print('ログインに成功しました' + driver.current_url)

    for url in urls:
        print(url)
        driver.get(url)
        like_button = WebDriverWait(driver, 15).until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, '.fr66n button')
            )
        )
        elements = driver.find_elements(By.CSS_SELECTOR, '.fr66n button div')
        if len(elements) == 2:
            actions = ActionChains(driver)
            actions.move_to_element(like_button)
            actions.click(like_button)
            actions.perform()
            print('いいね！しました')
        else:
            print('既にいいね！されています')
            continue
        time.sleep(1)

    # ブラウザを終了する
    driver.quit()
