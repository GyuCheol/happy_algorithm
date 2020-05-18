# '[닉네임] 님이 들어왔습니다
# '[닉네임] 님이 나갔습니다


def solution(records):
    logs = []
    name_map = {}

    # records 순회
    for r in records:
        # ' ' 공백으로 명령 분할 {action} {id} [{name}]
        cmds = r.split(' ')
        action = cmds[0]
        id = cmds[1]

        if action[0] == 'E': # Enter인 경우
            logs.append((id, '들어왔습니다.'))
            name_map[id] = cmds[2]
        elif action[0] == 'L': # Leave인 경우
            logs.append((id, '나갔습니다.''))
        else: # Change인 경우
            name_map[id] = cmds[2]

    # List Comprehension으로 logs에 기록된 내용 Converting  
    return [f'{name_map[id]}님이 {action}' for id, action in logs]

# formatting string
# a, b = 'A', 'C'
# f'{a}님이 {b}합니다.'
# '%s님이 %s합니다.' % (a, b)

print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))

