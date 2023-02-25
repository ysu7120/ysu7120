# metadata 모든 변수 불러오기
from insta.metadata import INSTAGRAM_LOGIN_ID, INSTAGRAM_LOGIN_PW, INSTAGRAM_LOGIN_CSS_ID, INSTAGRAM_LOGIN_CSS_PW, INSTAGRAM_LOGIN_CSS_BTN
from insta.metadata import FACEBOOK_LOGIN_ID, FACEBOOK_LOGIN_PW, FACEBOOK_LOGIN_CSS_ID, FACEBOOK_LOGIN_CSS_PW, FACEBOOK_LOGIN_CSS_BTN, FACEBOOK_LOGIN_CSS_BTN_OATH
from insta.metadata import LOGIN_OPTION, SEARCH_HASHTAG, POST_LENGTH, HEADER
from insta.metadata import CONTENT_URL, LOGIN_URL

# Selenium 모듈 불러오기
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

import time
from selenium.webdriver.common.by import By
import random

# Selenium 인스타그램 이메일 로그인
def insta_login(driver):
    login_ID = driver.find_element(By.CSS_SELECTOR, INSTAGRAM_LOGIN_CSS_ID)
    login_ID.send_keys(INSTAGRAM_LOGIN_ID)

    login_PW = driver.find_element(By.CSS_SELECTOR, INSTAGRAM_LOGIN_CSS_PW)
    login_PW.send_keys(INSTAGRAM_LOGIN_PW)

    driver.find_element(By.CSS_SELECTOR, INSTAGRAM_LOGIN_CSS_BTN).click()

# Selenium 인스타그램 페이스북 로그인
def facebook_login(driver):
    driver.find_element(By.CSS_SELECTOR, FACEBOOK_LOGIN_CSS_BTN_OATH).click()
    time.sleep(5)

    login_ID = driver.find_element(By.CSS_SELECTOR, FACEBOOK_LOGIN_CSS_ID)
    login_ID.send_keys(FACEBOOK_LOGIN_ID)

    login_PW = driver.find_element(By.CSS_SELECTOR, FACEBOOK_LOGIN_CSS_PW)
    login_PW.send_keys(FACEBOOK_LOGIN_PW)

    driver.find_element(By.CSS_SELECTOR, FACEBOOK_LOGIN_CSS_BTN).click()

# matadata.py의 LOGIN_OPTION의 값에 따라 작동하는 함수가 다릅니다.
def selenium_login(driver):
    if LOGIN_OPTION == 'instagram':  # 인스타그램 이메일 로그인
        insta_login(driver)

    elif LOGIN_OPTION == 'facebook':  # 페이스북 로그인
        facebook_login(driver)

    else:  # 옵션 잘못 설정했을 때
        print('Login Fail - CHECK metadata.py LOGIN_OPTION!!')
        driver.quit()

# Instagram이 반응형 웹이라 Selenium 사용
def selenium_postid_crawler(timer_len=500):
    # Selenium 크롬 드라이버 옵션
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--blink-settings=imagesEnabled=false')  # 크롬 이미지 불러오지 않게 처리
    chrome_options.add_argument('user-agent=' + HEADER['User-Agent'])  # 헤더 추가
    service=Service(ChromeDriverManager().install())  # 크롬 드라이버 자동 설치
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.set_window_size(750, 680)  # 크기 고정 (750 x 680)

    # 인스타그램 로그인 URL 접속
    driver.get(LOGIN_URL)  
    time.sleep(2)
    
    selenium_login(driver)
    time.sleep(10)

    # 해시태그 검색결과 URL로 이동
    driver.get(CONTENT_URL + SEARCH_HASHTAG)
    time.sleep(10)

    article, article_ids = [], []
    chk = 0
    height = 0

    # metadata.py의 POST_LENGTH의 값에 따라 작동 횟수가 달라집니다.
    # 검색결과의 각 post의 ID를 불러와 리스트(article_ids)에 저장
    while len(article_ids) <= POST_LENGTH:
        driver.find_element(By.CSS_SELECTOR, 'body').send_keys(Keys.HOME)

        for i in range(3):
            driver.find_element(By.CSS_SELECTOR, 'body').send_keys(Keys.END)
            time.sleep(random.uniform(2, 5))  # 너무 빠르게 스크롤을 내리면 로딩되지 않는 경우가 많음    
        
        article = driver.find_elements(By.XPATH, '//a[@href]')
        article = article[15:]
        
        for arti in article :
            arti_href = arti.get_attribute("href")
            try:
                article_ids.append(arti_href.split('/')[4])
            except:
                continue
        
        # 중복제거
        article_ids = list(set(article_ids))
        
        chk += 1
        
        if chk >= timer_len:  # 혹시나 발생한 로딩 오류를 위해 while문이 무한으로 돌아가지 않기 위한 조치
            print('지정 횟수 초과! IP 차단 혹은 로딩 오류 확인 요망.')
            break

    driver.quit()
    
    print(f'article_ids = {len(article_ids)}')

    return article_ids

