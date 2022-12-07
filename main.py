from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()

driver.get('https://google.co.kr')
driver.implicitly_wait(3)

search_box = driver.find_element_by_css_selector('.gLFyf')
search_box.send_keys('웨스트민스터 합창단')
search_box.send_keys(Keys.ENTER)
