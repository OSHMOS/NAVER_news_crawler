import time
import requests
import pandas as pd
from bs4 import BeautifulSoup
from openpyxl import Workbook
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

driver.get('https://google.co.kr')
time.sleep(2)

search_box = driver.find_element_by_css_selector('.gLFyf')
search_box.send_keys('북한인권정보센터')
search_box.send_keys(Keys.ENTER)
time.sleep(2)

news_tab_btn = driver.find_element_by_css_selector(
    '#hdtb-msb > div:nth-child(1) > div > div:nth-child(2) > a')
news_tab_btn.click()
time.sleep(2)

# wb = Workbook(write_only=True)
# ws = wb.create_sheet()
# ws.append(['제목', '링크'])


# LIMIT = 220
# url = f'https://www.google.co.kr/search?q=%22%EB%B6%81%ED%95%9C%EC%9D%B8%EA%B6%8C%EC%A0%95%EB%B3%B4%EC%84%BC%ED%84%B0%22&tbm=nws&sxsrf=ALiCzsaK4d-_mEpqj5QdWCu1nDvHYY_XDA:1670611316965&ei=dIGTY8K5OsOgoASWy6iQAw&start={LIMIT}'
# response = requests.get(url)
# search_page = response.text

search_page = driver.page_source

soup = BeautifulSoup(search_page, 'html.parser')
next_btn = soup.select_one(
    '#pnnext > span:nth-child(2)')
next_btn.click()
# next_btn.click()
# items = soup.select('.WlydOe')
# for item in items:
#     title = item.text
#     link = item.get('href')
#     ws.append([title, link])
# wb.save(f'북한인권정보센터 기사 스크랩.xlsx')

# driver.quit()
