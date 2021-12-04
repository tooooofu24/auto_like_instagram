import json
import requests
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as ECpython
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from const import URL
from const import PASSWORD
from const import USER_ID
from const import INSTAGRAM_API_URL


def login(driver):
    # ページにアクセス
    driver.get(URL + '/accounts/login/')
    print(driver.current_url)

    time.sleep(1)
    WebDriverWait(driver, 15).until(
        EC.visibility_of_element_located((By.XPATH, "/html/body/div[1]/section/main/div/div/div[1]/div/form/div/div[3]/button")))
    driver.find_element(By.NAME, "username").send_keys(USER_ID)
    driver.find_element(By.NAME, "password").send_keys(PASSWORD)
    login_btn = driver.find_element(
        By.XPATH, '/html/body/div[1]/section/main/div/div/div[1]/div/form/div/div[3]/button')

    actions = ActionChains(driver)
    actions.move_to_element(login_btn)
    actions.click(login_btn)
    actions.perform()
