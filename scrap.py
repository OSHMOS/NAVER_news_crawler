import requests
from bs4 import BeautifulSoup
from openpyxl import Workbook

# wb = Workbook(write_only=True)
# ws = wb.create_sheet()
# ws.append(['제목', '링크'])

LIMIT = 0
while True:
    url = f'https://www.google.co.kr/search?q=%22%EB%B6%81%ED%95%9C%EC%9D%B8%EA%B6%8C%EC%A0%95%EB%B3%B4%EC%84%BC%ED%84%B0%22&tbm=nws&sxsrf=ALiCzsaK4d-_mEpqj5QdWCu1nDvHYY_XDA:1670611316965&ei=dIGTY8K5OsOgoASWy6iQAw&start={LIMIT}'
    response = requests.get(url)
    search_page = response.text

    soup = BeautifulSoup(search_page, 'html.parser')
    items = soup.select('.WlydOe')
    if items == []:
        break
    print(items)
    # for item in items:
    #     title = item.text
    #     link = item.get('href')
    #     ws.append([title, link])

    LIMIT += 10

# wb.save('북한인권정보센터 기사 스크랩.xlsx')
