
class RoomRange():

    def __init__(self, begin, end):
        self.begin = begin
        self.end = end

def solution(k, room_number):
    room_dict = dict()
    answer = []

    for room in room_number:
        
        if room not in room_dict:
            answer.append(room)

            if room - 1 in room_dict:
                tmp = room_dict[room - 1]
                tmp.end = room
            else:
                tmp = RoomRange(room, room)

            room_dict[room] = tmp
            tmp_id = room + 1
            
        else:
            tmp = room_dict[room]
            tmp.end += 1
            answer.append(tmp.end)

            room_dict[tmp.end] = tmp

            tmp_id = tmp.end + 1

        # 연속된 다른 방의 range 참조 업데이트
        if tmp_id in room_dict:
            tmp.end = room_dict[tmp_id].end

            while tmp_id in room_dict:
                room_dict[tmp_id] = tmp
                tmp_id += 1

    return answer

# print(solution(10, [1, 3, 4, 1, 3, 1]))
# print(solution(10, [1, 3, 4, 5, 1, 1, 5]))

print(solution(10, [1, 3, 4, 5, 7, 9, 11, 13, 2, 5, 5]))