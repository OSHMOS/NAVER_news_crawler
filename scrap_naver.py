import csv
import time
import requests
from bs4 import BeautifulSoup

start = time.time()

csv_file = open('북한인권정보센터 기사 스크랩_naver.csv', 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['기사 제목', '기사 링크'])

LIMIT = 0
query = '북한인권정보센터'
while True:
    url = f'https://search.naver.com/search.naver?where=news&sm=tab_pge&query={query}&sort=1&photo=0&field=0&pd=0&ds=&de=&mynews=0&office_type=0&office_section_code=0&news_office_checked=&nso=so:dd,p:all,a:all&start={LIMIT}1'
    if 'start=3921' in url:
        break

    response = requests.get(url)
    search_page = response.text

    soup = BeautifulSoup(search_page, 'html.parser')

    news_titles = soup.select('a.news_tit')
    for news_title in news_titles:
        title = news_title.get_text()
        link = news_title.get('href')
        csv_writer.writerow([title, link])

    LIMIT += 1
csv_file.close()
end = time.time()
print(f'time : {end - start}')  # time : 117.44386577606201 sec
