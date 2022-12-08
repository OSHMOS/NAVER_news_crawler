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

search_page = driver.page_source
driver.quit()

soup = BeautifulSoup(search_page, 'html.parser')

wb = Workbook(write_only=True)
ws = wb.create_sheet()
ws.append(['제목', 'url'])

items = soup.select('.WlydOe')
for item in items:
    title = item.text
    link = item.get('href')
    ws.append([title, link])
wb.save('북한인권정보센터 기사 스크랩.xlsx')
