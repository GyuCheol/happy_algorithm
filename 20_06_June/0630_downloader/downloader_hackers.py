
# 해커스 인강 다운로드 해킹
# 인강 파일은 AquaPlayer Proxy를 통해 암호화된 동영상DRM 상태인데,
# 이것을 local에 설치된 PC Agent가 복호화하여 loopback으로 내 PC에 송출해준다.
# 이 원이를 이용하여 Proxy에게 가상의 HTTP Client로 mp4 파일을 달라고하여 복호화된 영상을 추출한다.
# 장장 6시간에 걸린 삽질...

# Partial된 mp4는 ffmpeg를 통해 merge한다.

import http
from http.client import HTTPConnection
from http.client import HTTPSConnection

host = 'cdnplayer.cdnetworks.com'
port = '8283'

# 각 영상마다 이 부분만 손댈 것.
url_list = [
    #'/cddr_dnp?url=%252F%25ED%2595%25B4%25EC%25BB%25A4%25EC%258A%25A4%2520%25EC%25B1%2594%25ED%2594%2584%25EC%258A%25A4%25ED%2584%25B0%25EB%2594%2594%252F%25ED%2586%25A0%25EC%259D%25B5%252F%25ED%2595%259C%2520%25EB%258B%25AC%2520%25EC%2595%2588%25EC%2597%2590%2520%25EB%2581%259D%25EB%2582%25B4%25EB%258A%2594%2520%25ED%2595%25B4%25EC%25BB%25A4%25EC%258A%25A4%2520%25ED%2586%25A0%25EC%259D%25B5%2520%25EA%25B8%25B0%25EC%25B6%259C%2520%25EB%25B3%25B4%25EC%25B9%25B4%2520%255B%25EC%25B5%259C%25EC%258B%25A0%25EA%25B0%259C%25EC%25A0%2595%25ED%258C%2590%255D%252F01%25EA%25B0%2595%2520%255BDAY%252001%255D%2520%25EC%25B1%2584%25EC%259A%25A9',
    '/cddr_dnp?url=%252F%25ED%2595%25B4%25EC%25BB%25A4%25EC%258A%25A4%2520%25EC%25B1%2594%25ED%2594%2584%25EC%258A%25A4%25ED%2584%25B0%25EB%2594%2594%252F%25ED%2586%25A0%25EC%259D%25B5%252F%25ED%2595%259C%2520%25EB%258B%25AC%2520%25EC%2595%2588%25EC%2597%2590%2520%25EB%2581%259D%25EB%2582%25B4%25EB%258A%2594%2520%25ED%2595%25B4%25EC%25BB%25A4%25EC%258A%25A4%2520%25ED%2586%25A0%25EC%259D%25B5%2520%25EA%25B8%25B0%25EC%25B6%259C%2520%25EB%25B3%25B4%25EC%25B9%25B4%2520%255B%25EC%25B5%259C%25EC%258B%25A0%25EA%25B0%259C%25EC%25A0%2595%25ED%258C%2590%255D%252F02%25EA%25B0%2595%2520%255BDAY%252002%255D%2520%25EA%25B7%259C%25EC%25B9%2599%2520%25C2%25B7%2520%25EB%25B2%2595%25EB%25A5%25A0',
]

conn = http.client.HTTPSConnection(host, port)

header = {
    'Accept-Encoding': 'identity;q=1, *;q=0',
    'Connection': 'keep-alive',
    'Host': 'cdnplayer.cdnetworks.com:8282',
    'Range': f'bytes=0-',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'
}

for i, url in enumerate(url_list):
    print(f'Progressing {i}.mp4...')
    conn.request('GET', url, '', header)

    resp = conn.getresponse()

    print(resp.status, resp.reason)
    print(resp.headers)

    # download
    with open(f'./{i}.mp4', 'wb') as f:
        f.write(resp.read())

    print(f'Finished {i}.mp4!')
    print()

# conn 끊기
conn.close()
