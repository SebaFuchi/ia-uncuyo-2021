import random
import math

class Board:
    def __init__(self, size):
        self.size = size
        
        self.board = []
        for i in range(self.size):
            self.board.append([])
            for j in range(self.size):
                node = Node()
                node.value = u"\u2B1C"
                node.y = i
                node.x = j
                self.board[i].append(node)

        queensPos = [n for n in range(0, self.size)]
        random.shuffle(queensPos) 
        self.queensNodes = []
        ## set queens
        for i in range(self.size):
            self.board[queensPos[i]][i].value = u"\u2B1B"
            self.queensNodes.append(self.board[queensPos[i]][i])

        self.h = self.get_h()


    def get_h(self):
        h = 0
        for i in range(self.size):
            for j in range(self.size):
                if self.board[j][i].value == u"\u2B1B":
                   h += self.check_cost(self.board[j][i])
        return math.trunc(h/2)
    
    def get_h_board(self):

        for i in range(self.size):
            queen = self.board[self.queensNodes[i].y][i]
            queen.value = u"\u2B1C"
            for j in range(self.size):
                newQueen = self.board[j][i]
                newQueen.value = u"\u2B1B"
                self.board[j][i].cost = self.get_h()
                newQueen.value = u"\u2B1C"
            queen.value = u"\u2B1B"


    def check_cost(self, node):
        cont = 0
        cont += self.check_hor(node)
        cont += self.check_diag(node)
        return cont


    def check_hor(self, node):
        cont = 0
        for i in range(self.size):
            if i != node.x:
                if self.board[node.y][i].value == u"\u2B1B":
                    cont += 1
        return cont

    def check_diag(self, node):
        leftD = True
        leftU = True
        rightU = True
        rightD = True

        cont = 0
        expand = 1
        x = node.x
        y = node.y
        while(leftD or leftU or rightD or rightU):

            if x + expand < self.size and y + expand < self.size:
                if self.board[y + expand][x + expand].value == u"\u2B1B":
                    cont += 1
            else:
                rightD = False

            if x - expand >= 0 and y - expand >= 0:
                if self.board[y - expand][x - expand].value == u"\u2B1B":
                    cont += 1
            else:
                leftU = False

            if x - expand >= 0 and y + expand < self.size:
                if self.board[y + expand][x - expand].value == u"\u2B1B":
                    cont += 1
            else:
                leftD = False


            if x + expand < self.size and y - expand >= 0:
                if self.board[y - expand][x + expand].value == u"\u2B1B":
                    cont += 1
            else:
                rightU = False

            expand += 1
        
        return cont
        


    def print_board(self):
        a = ""
        for k in range(len(self.board)):
            for j in range(len(self.board)):
                a += str(self.board[k][j].value)
            print(a)
            a = ""

    def print_cost(self):
        a = ""
        for k in range(len(self.board)):
            for j in range(len(self.board)):
                a += str(self.board[k][j].cost) + " "
            print(a)
            a = ""


class Node:
    value = None
    cost = None
    x = None
    y = None


