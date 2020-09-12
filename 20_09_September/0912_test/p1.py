import re

step_2nd = re.compile(r"[^a-z0-9\-_\.]")
step_3rd = re.compile(r"\.{2,}")


def solution(new_id):
    id = new_id

    # 1st process -> to lowercase
    id = id.lower()

    # 2nd
    id = ''.join(step_2nd.split(id))

    # 3rd
    id = '.'.join(step_3rd.split(id))

    # 4th
    if len(id) > 0 and id[0] == '.':
        id = id[1:]
    
    if len(id) > 0 and id[-1] == '.':
        id = id[:-1]
    
    # 5th
    if len(id) == 0:
        id = 'a'
    elif len(id) >= 16:
        # 6th
        id = id[:15]

        if id[-1] == '.':
            id = id[:-1]

    # 7th    
    while len(id) < 3:
        id += id[-1]
    

    return id


#print(solution("=.="))
#print(solution("...!@BaT#*..y.abcdefghijklm"))
#print(solution("z-+.^."))
#print(solution("123_.def"))
print(solution("abcdefghijklmn.p"))

