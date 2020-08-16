from collections import deque

class Node():
    
    def __init__(self):
        self.dict = dict()
        self.cnt = 0

class Trie():

    def __init__(self):
        self.root = Node()

    def add_word(self, word):
        
        tmp = self.root

        for ch in word:
            
            if ch not in tmp.dict:
                tmp.dict[ch] = Node()

            tmp = tmp.dict[ch]
            tmp.cnt += 1
        
    
    def find_word(self, query):
        q = deque()
        cnt = 0

        # 노드, step
        q.append((self.root, 0))

        while q:
            node, step = q.popleft()
            ch = query[step]

            if step == len(query):
                cnt += 1
            else:
                if ch == '?':
                    # '?'을 만나면 굳이 뒷 부분을 더 순회할 필요 없음.
                    # '?' 뒷 부분은 무조건 '?'이기 때문이다.
                    cnt += node.cnt
                else:
                    if ch in node.dict:
                        q.append((node.dict[ch], step + 1))

        return cnt
            
        
def solution(words, queries):
    trie = [None] * 10001
    reversed_trie = [None] * 10001

    for word in words:
        
        if trie[len(word)] == None:
            trie[len(word)] = Trie()
            reversed_trie[len(word)] = Trie()
        
        trie[len(word)].add_word(word)
        reversed_trie[len(word)].add_word(word[::-1])

    answer = []

    for query in queries:
        cnt = 0

        if trie[len(query)] != None:
        
            if query[0] == '?':
                # 접두사가 '?'라면 뒤집은 것으로 검색
                cnt += reversed_trie[len(query)].find_word(query[::-1])
            else:
                cnt += trie[len(query)].find_word(query)

        answer.append(cnt)

    return answer



solution(["frodo", "front", "frost", "frozen", "frame", "kakao"], ["fro??", "????o", "fr???", "fro???", "pro?"])
