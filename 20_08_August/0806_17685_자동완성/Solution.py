
class Node():

    def __init__(self):
        self.dict = dict()
        self.count = 1

class Tree():

    def __init__(self):
        self.root = Node()

    def add_word(self, word):
        
        tmp = self.root

        for ch in word:

            if ch in tmp.dict:
                tmp = tmp.dict[ch]
                tmp.count += 1
            else:
                t = Node()
                tmp.dict[ch] = t
                tmp = t


    def get_length_for_auto_comp(self, word):
        length = 0
        tmp = self.root

        for ch in word:
            length += 1

            if ch in tmp.dict and tmp.dict[ch].count > 1:
                tmp = tmp.dict[ch]
            else:
                break    

        return length



def solution(words):
    words_tree = Tree()
    answer = 0

    # init
    for word in words:
        words_tree.add_word(word)
    
    for word in words:
        answer += words_tree.get_length_for_auto_comp(word)

    return answer

print(solution(["word", "war", "warrior", "world"]))
print(solution(["abc", "def", "ghi", "jklm"]))
print(solution(["go", "gone", "guild"]))
