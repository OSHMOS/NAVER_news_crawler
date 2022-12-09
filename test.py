import requests
from bs4 import BeautifulSoup
from openpyxl import Workbook

url = 'https://www.google.co.kr/search?q=%22%EB%B6%81%ED%95%9C%EC%9D%B8%EA%B6%8C%EC%A0%95%EB%B3%B4%EC%84%BC%ED%84%B0%22&tbm=nws&sxsrf=ALiCzsaK4d-_mEpqj5QdWCu1nDvHYY_XDA:1670611316965&ei=dIGTY8K5OsOgoASWy6iQAw&start=230'
rep = requests.get(url)
test_page = rep.text

soup = BeautifulSoup(test_page, 'html.parser')

items = soup.select('.WlydOe')
print(items)
