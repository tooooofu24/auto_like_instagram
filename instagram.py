import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from const import URL
from const import PASSWORD
from const import USER_ID


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


def like(driver, url) -> bool:
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
        return True
    else:
        return False


def like_urls(driver, urls, count) -> int:
    for url in urls:
        if count >= 25:
            break
        print(url)
        driver.get(url)
        liked = like(driver, url)
        if liked == True:
            print('いいね！しました')
            count += 1
        else:
            print('既にいいね！しています')
        time.sleep(1)
    return count
