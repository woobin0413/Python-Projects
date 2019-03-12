# # -*- coding: utf-8 -*-
# # After log-in, go on personal account then shows the recent watched videos title
#
# from bs4 import BeautifulSoup as bs
# from selenium import webdriver
#
# options = webdriver.ChromeOptions()
# options.add_argument('headless')
# # options.add_argument('window-size=1440x900')
# options.add_argument("disable-gpu")
# # 혹은 options.add_argument("--disable-gpu")
# # UserAgent값을 바꿔줍시다!
# # options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36")
# # options.add_argument("lang=ko_KR") # 한국어!
#
#
#
# chrome_driver = webdriver.Chrome('../chromedriver')
#
# # lanuages 속성을 업데이트해주기
# chrome_driver.execute_script("Object.defineProperty(navigator, 'languages', {get: function() {return ['ko-KR', 'ko']}})")
# #
# # #암묵적 웹 자원 로드위해 3초 기다림
# chrome_driver.implicitly_wait(3)
#
# chrome_driver.get('https://www.facebook.com/login/')
#
#
# filename = 'auth2.txt'
# with open(filename) as f:
#     data = f.readlines()
#
#
# chrome_driver.find_element_by_name('pass').send_keys(data[1])
# chrome_driver.find_element_by_name('email').send_keys(data[0])
#
# chrome_driver.get('https://www.facebook.com/woobin.joo/allactivity?privacy_source=activity_log&log_filter=cluster_11&category_key=statuscluster')
#
# html = chrome_driver.page_source
# soup = bs(html, 'html.parser')
#
# watched_hist = soup.findAll('div', {'id': 'u_0_1f'})
# for list in watched_hist:
#     print(list)
#
from selenium import webdriver
from selenium.webdriver import ChromeOptions


options = ChromeOptions()
options.add_argument('headless')
options.add_argument('window-size=1440x900')
options.add_argument("disable-gpu")

driver = webdriver.Chrome('../chromedriver', chrome_options=options)

driver.get('http://naver.com')
driver.implicitly_wait(3)

driver.quit()