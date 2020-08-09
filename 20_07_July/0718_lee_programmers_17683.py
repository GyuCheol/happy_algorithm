# 7월 18일

# 방금그곡
# https://programmers.co.kr/learn/courses/30/lessons/17683
# 2018 카카오 블라인드 코딩테스트 3차 - lv2

# 문제 이해부터가 중요한 문제.
# 카카오 채용 문제는 지문이 굉장히 길고, 
# 문제에서 요구하는 다이나믹한 상황을 논리적으로 이해할 수 있어야 한다.
# 카카오 블라인드 채용 문제는 그게 핵심 같음.
# 문제 이해만 되어도 난이도가 그렇게 높다고 느껴지지 않을 문제들이 많다.

# 음악이 0~5라면 총 6글자가 된다는 것을 생각하자.
# 15:00 ~ 15:14라면 총 15글자가 될 수 있다는 것.
# 음악 길이와 악보의 길이가 일치하면 반복하지 않지만,
# 음악 길이가 짧다면 악보의 길이를 반복해서 나타내어야 한다
# 그 중의 일부를 들은 것일 수 있기 때문.

# 문자열을 쪼개어, 시간을 표현하고 (HH:MM)
# 1) 시간을 연산하여 음악 길이 구하기
# 2) 음악 길이와 악보 가지고 재생된 full 악보 만들기
# 3) m이 full 악보에 포함되는지 검사
# 4) 일치하는 악보 중 음악 시간, 음악 입력 순서 등으로 정렬해서 첫 값
# 5) 일치하는게 없다면 `(None)`
# lv2 문제 중에서도 난이도가 악랄해보인다. lv3는 되어 보이는데?

# 함정은 C# 같은 #이 있는 음이다.
# C#, D#, F#, G#, A#가 2글자라 1글자로 취급하는 다른 음과 계산에 문제가 생긴다.
# 그래서 다른 1글자로 변환 후 연산을 통합했다.
# 어이가 없는점.
# 문제지에 언급되지 않은 E#이 있다???? 이건 출제자의 잘못.
# None 문자열은 (None)으로 리턴해야한다. ??? 계속 ``을 감싸서 fail이었음..
# 문제지의 오류

# 시간 복잡도 : O(N^2) 아마 문자열 돌면서 문자열 연산까지 하기 때문?


def solution(m, musicinfos):
    l = []
    sharp_map = {
        'C': '!',
        'D': '@',
        'F': '#',
        'G': '$',
        'A': '%',
        'E': '^',
        'B': '&'
    }

    def convert_sharp_sound(s):
        tmp = []
        
        for ch in s:
            if ch == '#':
                tmp.append(sharp_map[tmp.pop()])
            else:
                tmp.append(ch)

        return ''.join(tmp)

    def get_minutes(hhmm):
        h, m = hhmm.split(':')

        return int(m) + (int(h) * 60)
    
    m = convert_sharp_sound(m)

    for id, info in enumerate(musicinfos):
        start, end, title, music = info.split(',')

        # hh:mm > 분 단위로 변환 후 플레이 타임 구하기
        playtime = get_minutes(end) - get_minutes(start)
        # playtime과 맞추기 위해 2글자 음을 1글자로 변환
        music = convert_sharp_sound(music)

        
        if playtime > len(music):
            full_music = music * (playtime // len(music)) + music[:playtime % len(music)]
        else:
            full_music = music[:playtime]

        # 얼핏 들은게 포함되었는가?
        if m in full_music:
            # 재생 시간, 순서 추가
            # 정렬 기준이 플레이 타임이 긴 > id 순서이기 때문에 음수로 저장
            l.append((-playtime, id, title))
    
    return '(None)' if len(l) == 0 else sorted(l)[0][2]

print(solution('ABC#', ['11:59,12:06,HELLO,ABC#', '11:59,12:14,HELLO2,ABC']))
print(solution('ABCDEFG', ['12:00,12:14,HELLO,CDEFGAB', '13:00,13:05,WORLD,ABCDEF']))
print(solution('CC#BCC#BCC#BCC#B', ['03:00,03:30,FOO,CC#B', '04:00,04:08,BAR,CC#BCC#BCC#B']))
