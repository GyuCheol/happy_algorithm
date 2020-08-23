
# 해커스 인강 다운로드 해킹
# 인강 파일은 암호화된 동영상DRM 상태인데,
# 이것을 local에 설치된 AquaPlayer PC Agent가 복호화하여 loopback으로 내 PC에 송출해준다.
# 이 원리를 이용하여 Proxy에게 가상의 HTTP Client로 mp4 파일을 달라고하면 복호화된 영상을 추출할 수 있다.

# 일반 브라우저는 header가 맞지 않아, Denied 상태가 되지만, 가상의 client로 header를 직접 개조하면 문제 없다.
# 장장 6시간에 걸린 삽질...
# 개인 목적으로 사용하자. (배포시 처벌된다)

import http
from urllib.parse import quote


path = '/해커스 챔프스터디/토익/[550점+목표] 해커스 토익 스타트 Listening 후반부/'

file_list = [
    '02강 [Part3] 11일 Course2 사내업무',
    '03강 [Part3] 12일 Course1 회의',

'04강 [Part3] 12일 Course2 사업 계획',

'05강 [Part3] 13일 Course1 고객 상담',

'06강 [Part3] 13일 Course2 시설 관리',

'07강 [Part3] 14일 Course1 쇼핑시설',

'08강 [Part3] 14일 Course2 편의시설',

'09강 [Part3] 15일 Course1 여가',

'10강 [Part3] 15일 Course2 교통 및 주거',

'11강 [Part3] Part Test 01 (01번~15번)',

'12강 [Part3] Part Test 02 (16번~39번)',

'13강 [Part4] 16일 Course1 음성메시지',

'14강 [Part4] 16일 Course2 자동 응답 시스템',

'15강 [Part4] 17일 Course1 사내 공지',

'16강 [Part4] 17일 Course2 공공 장소 공지',

'17강 [Part4] 18일 Course1 광고',

'18강 [Part4] 18일 Course2 라디오 방송',

'19강 [Part4] 19일 Course1 교통방송 및 일기예보',

'20강 [Part4] 19일 Course2 뉴스',

'21강 [Part4] 20일 Course1 행사연설',

'22강 [Part4] 20일 Course2 가이드의 안내',

'23강 [Part4] Part Test 01 (01번~15번)',

'24강 [Part4] Part Test 02 (16번~30번)',

'25강 [최신인강 업데이트] [Part 3] 2~3인 대화',

'26강 [최신인강 업데이트] Part 1&2 실수 줄이기',

'27강 [최신인강 업데이트] Part 3 최신경향 분석',

'28강 [최신인강 업데이트] Part2 함축 된 의미 파악하기',


]


host = 'cdnplayer.cdnetworks.com'
port = '8283'

conn = http.client.HTTPSConnection(host, port)

header = {
    'Accept-Encoding': 'identity;q=1, *;q=0',
    'Connection': 'keep-alive',
    'Host': f'{host}:{port}',
    'Range': f'bytes=0-',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'
}

for file_name in file_list:
    conn.request('GET', '/cddr_dnp?url=' + quote(path + file_name).replace('%', '%25'), '', header)

    print(f'Progressing {file_name}.mp4...')

    resp = conn.getresponse()

    print(resp.status, resp.reason)
    print(resp.headers)

    file_name2 = file_name.replace(' ', '_')

    # download
    with open(f'./{file_name2}.mp4', 'wb') as f:

        while True:
            buffer = resp.read(8192)

            f.write(buffer)

            if len(buffer) == 0:
                break


    print(f'Finished {file_name}.mp4!')
    print()

# conn 끊기
conn.close()
