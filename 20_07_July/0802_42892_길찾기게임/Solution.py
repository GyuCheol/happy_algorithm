import sys

sys.setrecursionlimit(1010)

class Node(object):

    def __init__(self, x, y, value):
        self.x = x
        self.y = y
        self.value = value
        self.left = None
        self.right = None

    # 정렬을 위한 < 연산자 오버로딩
    def __lt__(self, other):
        return self.y > other.y or (self.y == other.y and self.x < other.x)
    
    def search_pre(self, routine):
        routine.append(self.value)

        if self.left != None:
            self.left.search_pre(routine)
        
        if self.right != None:
            self.right.search_pre(routine)

    def search_post(self, routine):

        if self.left != None:
            self.left.search_post(routine)

        if self.right != None:
            self.right.search_post(routine)

        routine.append(self.value)


class Tree(object):

    def __init__(self):
        self.root = None
    
    def add_node(self, node):

        if self.root == None:
            self.root = node
            return

        tmp = self.root

        while True:

            if node.x < tmp.x:
                if tmp.left == None:
                    tmp.left = node
                    return
                else:
                    tmp = tmp.left
            else:
                if tmp.right == None:
                    tmp.right = node
                    return
                else:
                    tmp = tmp.right

    def find_preorder(self):
        routine = []

        self.root.search_pre(routine)

        return routine

    def find_postorder(self):
        routine = []

        self.root.search_post(routine)

        return routine


def solution(nodeinfo):
    sorted_node_list = sorted(map(lambda x: Node(x[1][0], x[1][1], x[0] + 1), enumerate(nodeinfo)))
    tree = Tree()

    for node_info in sorted_node_list:
        tree.add_node(node_info)

    return [tree.find_preorder(), tree.find_postorder()]

print(solution([[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]]))

tmp = []

for i in range(1000):
    tmp.append([i, i])

print(solution(tmp))
