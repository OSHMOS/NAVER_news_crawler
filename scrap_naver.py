import csv
import time
import requests
from bs4 import BeautifulSoup


def news_scrap():
    start = time.time()

    csv_file = open('네이버 뉴스 스크랩.csv', 'w')
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(['뉴스 제목', '뉴스 링크'])

    LIMIT = 0

    print('안녕하세요. 오스모스가 개발한 네이버 뉴스 크롤러입니다.')
    query = input('네이버 뉴스 키워드를 입력해주세요. : ')

    while True:
        url = f'https://search.naver.com/search.naver?where=news&sm=tab_pge&query={query}&sort=1&photo=0&field=0&pd=0&ds=&de=&mynews=0&office_type=0&office_section_code=0&news_office_checked=&nso=so:dd,p:all,a:all&start={LIMIT}1'
        if 'start=3991' in url:  # 네이버는 기사를 최대 4,000건까지만 제공한다.
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
    print(f'{end - start}초가 걸렸습니다.')
    print("'네이버 뉴스 스크랩.csv'를 시작 버튼을 눌러 검색해주세요.")


if __name__ == '__main__':
    news_scrap()
    ans = input("계속 사용을 원하시면 O를 입력해주세요. 이외의 것을 입력하시면 자동 종료됩니다. : ")
    if ans == 'O':
        news_scrap()
    else:
        print('프로그램이 종료되었습니다. 감사합니다.')
