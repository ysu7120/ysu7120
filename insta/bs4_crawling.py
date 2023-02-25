from insta.metadata import HEADER, PROXY_URL, POST_URL, SAVE_LENGTH, SEARCH_HASHTAG, EXT_PATH
from insta.utils import datetime_now, backup_numpy

# BeautifulSoup 모듈 불러오기
from bs4 import BeautifulSoup
from urllib import request
from urllib.request import urlopen

import pandas as pd
import time
import random
import re
import os

# IP 차단을 위한 무료 Proxy 리스트 불러오기
def load_proxy_list():
    req = request.Request(url=PROXY_URL, headers=HEADER)
    with urlopen(req) as response:
        proxy_html = response.read()
    proxy_soup = BeautifulSoup(proxy_html, 'html.parser')
    proxy_list = proxy_soup.select_one('textarea', class_='form-control').text.split('\n')[3:-1]
    return proxy_list

# 인스타그램 차단 방지용 proxy 실행
def setting_proxy(proxy):
    proxy_support = request.ProxyHandler({'http':proxy})
    opener = request.build_opener(proxy_support)
    opener.addheaders=list(zip(HEADER.keys(), HEADER.values()))
    request.install_opener(opener)

def save_csv(save_path, post_dict, article_ids, i):
    df = pd.DataFrame.from_dict(post_dict, orient='index').T
    df.to_csv(f'{save_path}{str(len(article_ids))} instagram_crawling.csv', mode='w', index=False)
    df.to_csv(f'{save_path}1 ~ {str(i)} instagram_crawling.csv', mode='w', index=False)  # metadata.py에서 지정한 SAVE_LENGTH 변수 만큼만 csv파일 저장

def add_csv(save_path, post_dict, article_ids, i, end):
    df = pd.DataFrame.from_dict(post_dict, orient='index').T
    df.to_csv(f'{save_path}{str(len(article_ids))} instagram_crawling.csv', mode='a', index=False, header=False)
    if end == False:
        df.to_csv(f'{save_path}{str(i - SAVE_LENGTH + 1)} ~ {str(i)} instagram_crawling.csv', mode='w', index=False)  # metadata.py에서 지정한 SAVE_LENGTH 변수 만큼만 csv파일 저장
    elif end == True:
        df.to_csv(f'{save_path}{str(i - (i % SAVE_LENGTH) + 1)} ~ {str(i + 1)} instagram_crawling.csv', mode='w', index=False)  # metadata.py에서 지정한 SAVE_LENGTH 변수 만큼만 csv파일 저장

def bs4_crawler(article_ids):
    # Pandas로 빠르게 변환할 수 있도록 dictionary 사용
    post_dict = {'post_id':[], 'name':[], 'post':[], 'hashtag':[]}
    error_count = 0  # 게시글 에러 카운트
    count_429_max = 3  # 429 에러 발생시 재시도 횟수
    count_proxy_max = 5  # 프록시 횟수 제한
    proxy_list = load_proxy_list()
    save_path = f'{EXT_PATH}{datetime_now()} {SEARCH_HASHTAG}/'
    backup_numpy(article_ids, save_path)

    for i in range(len(article_ids)):
        post_html = None
        insta_soup = None
        req = None
        count_429 = 0  # Instagram은 일정 시간동안 너무 많은 요청을 보내면 차단되는 경우가 있음.
        count_proxy = 0

        # post_html에 값이 없다면 반복
        while not post_html:
            # IP 차단 혹은 불안정한 인터넷 상황 고려
            try:
                req = request.Request(POST_URL+article_ids[i], headers=HEADER)
                with urlopen(req) as response:
                    post_html = response.read()
                insta_soup = BeautifulSoup(post_html, 'html.parser')
            except:
                print(f'{i + 1}번째 작업 중 429 http 에러 발생. 재시도 횟수: {count_429 + 1}')

                count_429 += 1
                
                time.sleep(random.uniform(5, 10))
                
            # count_429_max 로 지정한 횟수가 끝날 때까지 에러 발생시 랜덤 proxy로 변경 후 재시도
            if count_429 >= count_429_max:
                count_429 = 0
                proxy = random.choice(proxy_list)  # 프록시 랜덤 적용
                print(f'{i + 1}번째 작업 중 429 http 에러 발생. {count_429_max}회 재시도 했으나 반응이 없어 Proxy 변경 후 재시도합니다.')
                print(f'사용 Proxy 주소: {proxy}')
                setting_proxy(proxy)  
                count_proxy += 1
            
            # count_proxy_max 로 지정한 횟수가 끝날 때까지 에러 발생시 다음 게시글로 넘어가도록 while문 탈출
            if count_proxy >= count_proxy_max:
                print(f'{i + 1}번째 작업 중 429 http 에러 발생. {count_proxy_max}회 프록시 변경 후 재시도 했으나 실패하여 다음 게시글로 넘어갑니다.')
                break
                
        # 크롤링 도중 삭제된 게시글 고려
        try:  # 삭제되지 않아 정상적으로 크롤링 되었다면 실행
            post_string = insta_soup.select_one('meta[property="og:title"]')['content']
            name = post_string.split('"')[0].split()[0]
            post = post_string.split('"')[1]
            hashtag = re.compile('#\w{1,}').findall(post_string)
            
            post_dict['post_id'].append(article_ids[i])
            post_dict['name'].append(name)
            post_dict['post'].append(post)
            post_dict['hashtag'].append(hashtag)
            print(f'{i + 1}. {article_ids[i]} 완료')
        
        except:  # 크롤링 도중 삭제되어 정상적으로 크롤링되지 않았을 때 실행
            print(f'{i + 1}. {article_ids[i]} 에러')
            error_count += 1
            continue
            
        if i != 0:
            # instagram_crawling.csv 파일이 없고 0번째 게시글 id가 아니며 metadata.py에서 지정한 SAVE_LENGTH 변수만큼 크롤링했을 때 csv파일 저장
            if not os.path.exists(f'{save_path}{len(article_ids)} instagram_crawling.csv') and i % SAVE_LENGTH == 0:
                save_csv(save_path, post_dict, article_ids, i)
                post_dict = {'post_id':[], 'name':[], 'post':[], 'hashtag':[]}
            
            # 지정한 변수만큼 크롤링했을 때 csv파일 저장
            elif i % SAVE_LENGTH == 0:
                add_csv(save_path, post_dict, article_ids, i, end = False)
                post_dict = {'post_id':[], 'name':[], 'post':[], 'hashtag':[]}
        
        elif i == 500:
            time.sleep(60 * 30)

        time.sleep(random.uniform(3, 5))

    # 마지막까지 크롤링 완료 시 csv파일 저장 및 결과 출력     
    add_csv(save_path, post_dict, article_ids, i, end = True)
    print(f'작업완료 총 {len(article_ids)} 개, 에러 {error_count} 개')

    return save_path
