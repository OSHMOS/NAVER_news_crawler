import csv
import requests
from datetime import datetime
from bs4 import BeautifulSoup


csv_file = open('().csv', 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['뉴스 제목', '뉴스 링크', '언론사', '날짜'])

url = 'https://search.naver.com/search.naver?where=news&sm=tab_pge&query="북한인권정보센터"&sort=1&photo=0&field=0&pd=0&ds=&de=&mynews=0&office_type=0&office_section_code=0&news_office_checked=&nso=so:dd,p:all,a:all&start=1'
rep = requests.get(url)
test_page = rep.text

soup = BeautifulSoup(test_page, 'html.parser')

news_titles = soup.select('a.news_tit')
info_group = soup.select('div.info_group')
for news_title, info in zip(news_titles, info_group):
    title = news_title.get_text()
    link = news_title.get('href')
    # press = info.get_text()
    span = info.select('span.info')
    if len(span) > 1:
        date = span[-1].get_text()
    else:
        date = span[0].get_text()
    if '분 전' in date or '시간 전' in date:
        date = f'{datetime.now().year}-{datetime.now().month}-{datetime.now().day}'
    elif '일 전' in date and int(date[0]) > 0:
        date = f'{datetime.now().year}-{datetime.now().month}-{datetime.now().day - int(date[0])}'
    print(date)
