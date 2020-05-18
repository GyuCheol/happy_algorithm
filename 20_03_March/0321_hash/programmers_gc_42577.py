
def solution(phone_book):
    
    length_set = {len(x) for x in phone_book}
    book_set = {x for x in phone_book}
    
    # 3, 8, 10

    for phone in phone_book:
        for l in length_set:
            if len(phone) > l and phone[:l] in book_set:
                return False
        
    return True


print(solution(['119', '12341234', '1191234123']))
