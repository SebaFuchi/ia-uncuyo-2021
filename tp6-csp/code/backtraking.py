import time

class BTraking:
    def __init__(self,size):
        self.size = size
        self.states = 0


    def find_solution(self):
        start_time = time.time()
        for i in range(0, self.size):
            res = self.recurs_solv([i])
            if res != False:
                # self.print_board(res)
                final_time = time.time() - start_time
                return (res, self.states, final_time)
        return




    def recurs_solv(self,queens):
        self.states += 1
        for i in range(0, self.size):
            if i not in queens:
                queens.append(i)
                if self.get_h(queens) == 0:
                    if len(queens) == self.size:
                        return queens

                    result = self.recurs_solv(queens)

                    if result != False:
                        return result

                queens.pop()
        
        return False



    def get_h(self,queens):
        h = 0
        des_diag = []
        asc_diag = []
        ##queens = ''.join(queens)
        for i in range(len(queens)):
            elem1 = int(queens[i]) - i
            des_diag.append(elem1)

            elem2 = int(queens[i]) + i
            asc_diag.append(elem2)

            for j in range(i+1,len(queens),1):
                if queens[i] == queens[j]:
                    h +=1

        for i in range(len(queens)):
            for j in range(i + 1, len(queens), 1):
                if des_diag[i] == des_diag[j]:
                    h += 1
                if asc_diag[i] == asc_diag[j]:
                    h += 1
        return h


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