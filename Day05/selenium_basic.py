from selenium import webdriver
import time

# 다운로드 받은 크롬 물리드라이버 가동 명령
driver = webdriver.Chrome('C:/Users/Sungjin/Desktop/JAVA_WEP/python/chromedriver.exe')

# 물리 드라이버로 사이트 이동 명령
driver.get('https://www.naver.com')