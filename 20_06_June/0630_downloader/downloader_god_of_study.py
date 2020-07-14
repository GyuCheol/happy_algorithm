
# 공신닷컴 인강 추출은 해커스 인강에 비해 심플함.
# 공신 닷컴은 Vimeo라는 cdn 경제적인 플랫폼으로 영상을 송출하기에
# 영상 추출이 해커스인강에 비해 비교적 쉽다.
# 다만 Vimeo도 token 방식으로 영상을 송출하기에, 인증된 아이디로 먼저 토큰을 따두어야 한다.

# 백준 인강도 Vimeo이므로 이 방법으로 추출이 가능하다.
# POCU도 마찬가지

# 여러 연구를 했지만, javascript 로딩을 통해 mp4 링크를 얻기 때문에
# virtual http client로는 한계가 있는 것 같다.
# 노가다...

from http.client import HTTPSConnection
from urllib.parse import quote
from re import findall


conn = HTTPSConnection('www.gongsin.com')
url = ''

headers = {
    'content-type': 'application/x-www-form-urlencoded',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'
}

# login 토큰 얻기
def get_token():
    conn.request('GET', '/login')

    resp = conn.getresponse()

    print(resp.status)

    html = str(resp.read())

    l = findall('name="_token" value="(.*?)"', html)

    return l[0]


# login session 활성화
def create_login_session():
    body = bytes(quote(f'_token={token}&username=gyuc219&password=a141141E%21&remember=on'), 'utf8')

    conn.request('POST', '/login', body, headers)
    resp = conn.getresponse()
    resp.read()

    print(resp.status)

def extract_mp4_links():
    

    for link in lectures:
        conn.request('GET', f'/lessons/{link}')

        resp = conn.getresponse()

        print(resp.status)

        html = resp.read().decode('utf-8')

        print(html)


lectures = ['3632']

token = get_token()
create_login_session()
extract_mp4_links()

conn.close()
