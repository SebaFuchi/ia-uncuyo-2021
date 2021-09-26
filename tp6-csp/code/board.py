class Board:
    def __init__(self, size):
        self.size = size
        self.slots = []

        for i in range(0, self.size):
            self.slots.append([n for n in range(0, self.size)])

    def print_board(self, queensPos):
        board = []
        for i in range(self.size):
            board.append([])
            for j in range(self.size):
                node = Node()
                node.value = u"\u2B1C"
                node.y = i
                node.x = j
                board[i].append(node)

        queensNodes = []
        for i in range(self.size):
            board[queensPos[i]][i].value = u"\u2B1B"
            queensNodes.append(board[queensPos[i]][i])


        a = ""
        for k in range(len(board)):
            for j in range(len(board)):
                a += str(board[k][j].value)
            print(a)
            a = ""

class Node:
    value = None
    cost = None
    x = None
    y = None


