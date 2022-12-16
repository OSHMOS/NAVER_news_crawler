# step1.selenium 패키지와 time 모듈 import
import time
import csv
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

start = time.time()

csv_file = open('북한인권정보센터 기사 스크랩_naver.csv', 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['기사 제목', '기사 링크'])

# step2.검색할 키워드 입력
query = '북한인권정보센터'

# step3.크롬드라이버로 원하는 url로 접속
url = 'https://www.naver.com/'
driver = webdriver.Chrome()
driver.get(url)
time.sleep(3)

# step4.검색창에 키워드 입력 후 엔터
search_box = driver.find_element_by_css_selector("input#query")
search_box.send_keys(query)
search_box.send_keys(Keys.RETURN)
time.sleep(2)

# step5.뉴스 탭 클릭 (검색어에 따라서 맨 마지막 대괄호 숫자만 바꿔주면 된다.)
driver.find_element_by_xpath('//*[@id="lnb"]/div[1]/div/ul/li[8]/a').click()
time.sleep(2)

# step6.최신순 탭 클릭
driver.find_element_by_xpath('//*[@id="snb"]/div[1]/div/div[1]/a[2]').click()
time.sleep(2)

while True:
    news_titles = driver.find_elements_by_css_selector('a.news_tit')
    for news_title in news_titles:
        title = news_title.text
        link = news_title.get_attribute('href')
        csv_writer.writerow([title, link])

    # step7.다음 페이지로 가는 버튼 클릭
    next_btn = driver.find_element_by_xpath(
        '//*[@id="main_pack"]/div[2]/div/a[2]')
    next_href = next_btn.get_attribute('href')
    next_btn.click()
    time.sleep(2)

    if next_href:
        continue
    else:
        break
csv_file.close()
end = time.time()
print(f'time : {end - start}')  # time : 1000.122661113739 sec
driver.quit()
