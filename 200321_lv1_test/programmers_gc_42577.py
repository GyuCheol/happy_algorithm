

def solution(phone_book):
    
    length_list = {len(x) : True for x in phone_book}
    book_map = {x : True for x in phone_book}
    
    for phone in phone_book:
        for l in length_list:
            if len(phone) > l and phone[0:l] in book_map:
                return False
        
    return True


print(solution(['119', '123', '11945123']))
