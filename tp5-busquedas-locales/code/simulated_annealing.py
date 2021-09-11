from operator import itemgetter
import board
import random
import math

class Climber:
    def __init__(self, size):
        self.state = board.Board(size)
        self.h = self.state.get_h()
        self.time = 1

    def solution_finder(self):
        self.state.print_board()
        self.state.get_h_board()
        print()
        print("H actual: " + str(self.h))
        print("COSTO INICIAL")
        self.state.print_cost()

        print()

        cont = 0

        while self.time < 1000:
            cont += 1
            self.new_state()
            self.state.get_h_board()
        print()

        self.state.print_board()

        print("H actual: " + str(self.h))
        print("Numero de iteraciones llevadas a cabo: " + str(cont))
        print("COSTO ACTUAL")
        self.state.print_cost()

    def new_state(self):
        board = self.state.board
        nodes = []

        for i in range(self.state.size):
            nodes.extend(board[i])

        flag = True
        while flag:
            if len(nodes) == 0:
                break
            rnd = random.randint(0, len(nodes)-1)
            element = nodes.pop(rnd)
            if element.value !=  u"\u2B1B":
                dif = self.h - element.cost
                if dif > 0:
                    self.h = element.cost
                    element.value = u"\u2B1B"
                    self.state.queensNodes[element.x] = u"\u2B1C"
                    self.state.queensNodes[element.x] = element
                    flag = False
                else:
                    prob = 1/self.time
                    num = random.uniform(0, 1)
                    if num < prob:
                        self.h = element.cost
                        element.value = u"\u2B1B"
                        self.state.queensNodes[element.x] = u"\u2B1C"
                        self.state.queensNodes[element.x] = element
                        flag = False

        self.time +=2
        return
