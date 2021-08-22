import random
import math


class Environment:
    def __init__(self):
        obstacles_rate = 0.2
        self.size = 10
        self.table = []
        for i in range(self.size):
            self.table.append([])
            for j in range(self.size):
                node = Node()
                node.y = i
                node.x = j
                node.value = u"\u2B1C"
                node.cost = random.randint(0, 25)
                self.table[i].append(node)
        obstacles = math.ceil((self.size * self.size) * obstacles_rate)
        while obstacles > 0:
            x = random.randint(0, (self.size)-1)
            y = random.randint(0, (self.size)-1)
            if (self.table[y][x].value == u"\u2B1C"):
                self.table[y][x].value = u"\u2B1B"
                obstacles -= 1

        while True:
            startX = random.randint(0, (self.size)-1)
            startY = random.randint(0, (self.size)-1)
            if self.table[startY][startX].value == u"\u2B1C":
                self.table[startY][startX].value = u"\U0001F7E7"
                self.startNode = self.table[startY][startX]
                self.startX = startX
                self.startY = startY
                self.actX = startX
                self.actY = startY
                break

        while True:
            endX = random.randint(0, (self.size)-1)
            endY = random.randint(0, (self.size)-1)
            if self.table[endY][endX].value == u"\u2B1C":
                self.table[endY][endX].value = u"\U0001F7E5"
                self.endNode = self.table[endY][endX]
                break

    def print_enviroment(self):
        a = ""
        for k in range(len(self.table)):
            for j in range(len(self.table)):
                a += str(self.table[k][j].value)
            print(a)
            a = ""



class Node:
    value = None
    x = None
    y = None
    cost = None
