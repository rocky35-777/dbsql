from selenium import webdriver

(1) 상대경로
path = "./chromedriver"

(2) 절대경로
import os
path = os.getcwd() + "/chromedriver"

browser = webdriver.Chrome() # 경로지정
browser.get("http://naver.com")

(3) 기본함수
browser.back() # 뒤로가기
browser.forward() # 앞으로가기
browser.refresh() # 새로고침