# 사용할 계정의 ID/PW
INSTAGRAM_LOGIN_ID = ''
INSTAGRAM_LOGIN_PW = ''
FACEBOOK_LOGIN_ID = ''
FACEBOOK_LOGIN_PW = ''

LOGIN_OPTION = 'instagram'  # 로그인 방법 선택 instagram / facebook
SEARCH_HASHTAG = '크리스마스'  # 검색할 해시태그

POST_LENGTH = 5000  # 불러올 게시글 갯수
SAVE_LENGTH = 100  # 지정한 게시글 갯수 마다 csv 저장

# 저장경로
EXT_PATH = './'
DONG_PATH = './dong_utf.csv'

# 헤더
HEADER = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/7046A194A'}

# URL
CONTENT_URL = "https://www.instagram.com/explore/tags/"
LOGIN_URL = 'https://www.instagram.com/accounts/login/'
POST_URL = 'https://www.instagram.com/p/'
PROXY_URL = "https://free-proxy-list.net/"

# Selector INFO
INSTAGRAM_LOGIN_CSS_ID = '#loginForm > div > div:nth-child(1) > div > label > input'
INSTAGRAM_LOGIN_CSS_PW = '#loginForm > div > div:nth-child(2) > div > label > input'
INSTAGRAM_LOGIN_CSS_BTN = '#loginForm > div > div:nth-child(3) > button'

FACEBOOK_LOGIN_CSS_ID = '#email'
FACEBOOK_LOGIN_CSS_PW = '#pass'
FACEBOOK_LOGIN_CSS_BTN_OATH = '#loginForm > div > div:nth-child(5) > button'
FACEBOOK_LOGIN_CSS_BTN = '#loginbutton'
