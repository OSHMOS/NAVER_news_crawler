import requests
from bs4 import BeautifulSoup

url = 'https://www.google.co.kr/search?q=%EB%B6%81%ED%95%9C%EC%9D%B8%EA%B6%8C%EC%A0%95%EB%B3%B4%EC%84%BC%ED%84%B0&source=lnms&tbm=nws&sa=X&ved=2ahUKEwjW-vj3z-n7AhUB0GEKHZ0vAFYQ_AUoAXoECAEQAw&biw=1200&bih=707&dpr=2'
response = requests.get(url)
search_page = response.text

soup = BeautifulSoup(search_page, 'html.parser')
first_news = soup.select_one('.SoaBEf')
print(first_news)
