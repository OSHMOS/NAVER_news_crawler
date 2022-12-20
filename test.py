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
info_groups = soup.select('a.info.press')
info_list = soup.select('span.info')
print(info_group)
for news_title, info_group, info in zip(news_titles, info_groups, info_group):
    title = news_title.get_text()
    link = news_title.get('href')
    press = info_group.get_text()
    span = info.select('span.info')
    if len(span) > 1:
        span = span[-1]
    else:
        span = span[0]
    print(span)
    # csv_writer.writerow([title, link, press, date])
# csv_file.close()
