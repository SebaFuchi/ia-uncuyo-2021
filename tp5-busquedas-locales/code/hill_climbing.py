from operator import itemgetter
import board

class Climber:
    def __init__(self, size):
        self.state = board.Board(size)
        self.h = self.state.get_h()


    def solution_finder(self):
        self.state.print_board()
        self.state.get_h_board()
        print()
        print("H actual: " + str(self.h))
        print("COSTO INICIAL")
        self.state.print_cost()

        print()
        maxIt= 10
        cont = 0

        while maxIt > 0:
            if self.new_state() == False:
                break
            cont += 1
            maxIt -= 1
        print()

        self.state.print_board()

        print("H actual: " + str(self.h))
        print("Numero de iteraciones llevadas a cabo: " + str(cont))
        print("COSTO ACTUAL")
        self.state.print_cost()


    def new_state(self):
        board = self.state.board
        min_h = []
        node = None
        for i in range(self.state.size):
            min = self.h
            for j in range(self.state.size):
                element = board[j][i]
                if element.cost < min:
                    min = element.cost
                    node = element

            if min < self.h:
                min_h.append((node, min))


        min_h = sorted(min_h,key=itemgetter(1))
        if len(min_h) == 0:
            return False
        element = min_h.pop(0)
        self.h = element[1]
        

        element[0].value = u"\u2B1B"

        self.state.queensNodes[element[0].x] = u"\u2B1C"
        self.state.queensNodes[element[0].x] = element[0]

        self.state.get_h_board()

        return True

