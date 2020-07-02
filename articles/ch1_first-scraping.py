import time
from selenium import webdriver

# 仮想ブラウザ起動、URL先のサイトにアクセス
driver = webdriver.Chrome()
driver.get('https://www.google.com/')
time.sleep(2)

# サイト内から検索フォームを探す。
# Googleでは検索フォームのNameが「q」です。
el = driver.find_element_by_name("q")
# 検索フォームに文字を入力
el.send_keys('Qiitaで記事投稿楽しいぞ！！！')
time.sleep(2)

# 検索フォーム送信（Enter）
el.submit()

from bs4 import BeautifulSoup
soup = BeautifulSoup(driver.page_source, features="html.parser")
# タイトルをターミナル上に表示
print(soup.title.string)