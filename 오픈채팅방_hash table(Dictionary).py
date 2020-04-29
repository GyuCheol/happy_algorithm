# '[닉네임] 님이 들어왔습니다
# '[닉네임] 님이 나갔습니다


tmp = {
    'Enter' : '들어왔습니다.',
    'Leave': '나갔습니다.'
}

def solution(records):
    log = []
    d = {}

    for r in records:
        cmds = r.split(' ')
        action = cmds[0]
        id = cmds[1]

        if action[0] == 'E':
            log.append((id, action))
            d[id] = cmds[2]
        elif action[0] == 'L':
            log.append((id, action))
        else:
            d[id] = cmds[2]
            
    return [f'{d[id]}님이 {tmp[action]}' for id, action in log]

# formatting string
# a, b = 'A', 'C'
# f'{a}님이 {b}합니다.'
# '%s님이 %s합니다.' % (a, b)

print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))


