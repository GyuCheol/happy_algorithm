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