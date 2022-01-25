import time
import instagram
import json
from const import TAG_ID_1
from const import TAG_ID_2
from const import TAG_ID_3
import selenium_lib


def lambda_handler(event=None, context=None):

    driver = selenium_lib.setup()

    print('ログインします')
    instagram.login(driver)
    time.sleep(5)
    print('ログインに成功しました' + driver.current_url)

    urls = selenium_lib.getUrls(TAG_ID_1)
    print('#大学生の勉強垢の新規投稿が'+str(len(urls))+'件見つかりました')
    print(urls)

    count = 0
    count = instagram.like_urls(driver, urls, count)
    print(str(count)+'件の投稿にいいねしました')

    if(count < 25):
        urls = selenium_lib.getUrls(TAG_ID_2)
        print('#大学生活の新規投稿が'+str(len(urls))+'件見つかりました')
        print(urls)
        count = instagram.like_urls(driver, urls, count)
        print(str(count)+'件の投稿にいいねしました')
    if(count < 25):
        urls = selenium_lib.getUrls(TAG_ID_3)
        print('#大学生の新規投稿が'+str(len(urls))+'件見つかりました')
        print(urls)
        count = instagram.like_urls(driver, urls, count)
        print(str(count)+'件の投稿にいいねしました')

    print('いいねを終了します')

    # ブラウザを終了する
    driver.quit()

    return {
        'statusCode': 200,
        'body': json.dumps('正常に終了しました')
    }


if __name__ == '__main__':
    lambda_handler()
