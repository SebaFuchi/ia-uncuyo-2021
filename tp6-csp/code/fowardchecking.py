import board
import copy
import time

class Foward:
    def __init__(self,size):
        self.size = size
        self.board = board.Board(size)
        self.states = 0

    def find_solution(self):
        start_time = time.time()
        colum = self.board.slots[0]
        for element in colum:
            result = self.recurs_solv(0, element, copy.deepcopy(self.board))
            if result != False and result != None:
                result.reverse()
                #self.board.print_board(result)
                final_time = time.time() - start_time
                return (result,self.states,final_time)
        
                


    def recurs_solv(self,x, element, board):
        
        if x + 1 == self.size:
            return [element]

        res = self.foward_checker(x + 1, element, element - 1, element + 1, board)
        if res == True:
            colum = board.slots[x+1]
            if len(colum) == 0:
                return None

            for new_elem in colum:
                self.states += 1
                result = self.recurs_solv(x+1, new_elem, copy.deepcopy(board)) 

                if result == False:
                    return False

                if result != None:
                    result.append(element)
                    return result
                

        return


    def foward_checker(self,x,y,diag_sup, diag_inf, board):
        start = x

        for i in range(start, self.size):
            colum = board.slots[x]

            if len(colum) == 0:
                return False

            if y in colum:
                colum.remove(y)

            if diag_sup >= 0 and diag_sup in colum:
                colum.remove(diag_sup)

            if diag_inf < self.size and diag_inf in colum:
                colum.remove(diag_inf)

            x += 1
            diag_sup -= 1
            diag_inf += 1

        for i in board.slots:
            if len(i) == 0:
                return False

        return True
