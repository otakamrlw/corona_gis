URL      = "https://r.nikkei.com/search?keyword=%E9%99%A2%E5%86%85%E6%84%9F%E6%9F%93" # <= ここにスクレイピングしたい対象URLを書いてください
Selector = "h1.nl-Hero_title"  # <= ここにスクレイピングしたい対象のCSSセレクタを書いてください

# 必須
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

# Selenium用オプション
op = Options()
op.add_argument("--disable-gpu");
op.add_argument("--disable-extensions");
op.add_argument("--proxy-server='direct://'");
op.add_argument("--proxy-bypass-list=*");
op.add_argument("--start-maximized");
op.add_argument("--headless");
driver = webdriver.Chrome(chrome_options=op)

# Seleniumでサイトアクセス
# スクレイピングしたい対象が描写されるまでWait
# time.sleep()はご法度！指定した時間待っても描写されない事はままあるので。
driver.get(URL)
WebDriverWait(driver, 30).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, Selector))
)

soup = BeautifulSoup(driver.page_source, features="html.parser")
el = soup.select(Selector)[0].string
print(el)