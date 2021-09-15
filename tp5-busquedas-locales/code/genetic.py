import random
import time
from operator import itemgetter

class Genetic:
    def __init__(self,size):
        self.population = []
        self.size = size
        self.worse = 0
        for i in range(size-1):
            self.worse += (size-1)-i

        for i in range(100):
            b = Board(size)
            self.population.append(b)


    def solution(self):
        start_time = time.time()

        self.best = None
        self.best_fit = self.worse
        self.best_iteration = None
        self.h_to_g = []
        for i in range(200):
            self.new_population()
            self.select_best(i)

        final_time = time.time() - start_time
        return (self.best.get_h(), self.best_iteration, final_time, self.h_to_g)


    def solution_finder(self):
        print()
        print("POBLACION INICIAL")
        print("-----------------")
        print()

        for i in range(len(self.population)):
            self.population[i].print_board()
            print(self.population[i].get_h())
            print()

        self.best = None
        self.best_fit = self.worse
        self.best_iteration = None
        self.h_to_g = []
        for i in range(200):
            self.new_population()
            self.select_best(i)

        return self.best

    def new_population(self):
        new_population = []

        for i in range(int(len(self.population)/2)):
            parents = self.select_parents()
            childs = self.reproduce(parents)
            new_population.extend(childs)
            olds = self.preserve_bests()
            survivers = self.kill_them_all(new_population)

        olds.extend(survivers)
        self.population = olds


    def select_parents(self):
        element1 = None
        element2 = None
        while element1 == None:
            rnd1 = random.randint(0, len(self.population)-1)
            rnd2 = random.uniform(0, 1)
            fitnees = self.worse - self.population[rnd1].get_h()
            prob = fitnees / self.worse

            if rnd2 <= prob:
                element1 = self.population[rnd1]

        while element2 == None:
            rnd1 = random.randint(0, len(self.population)-1)
            rnd2 = random.uniform(0, 1)
            fitnees = self.worse - self.population[rnd1].get_h()
            prob = fitnees / self.worse

            if rnd2 <= prob and self.population[rnd1].queensPos != element1.queensPos:
                element2 = self.population[rnd1]

        return (element1,element2)

    def reproduce(self, parents):
        cut = random.randint(0, self.size - 1)

        child1 = parents[0].queensPos[:cut] + parents[1].queensPos[cut:]
        child1 = self.mutate(child1)
        b1 = Board(self.size)
        b1.queensPos = child1

        child2 = parents[1].queensPos[:cut] + parents[0].queensPos[cut:]
        child2 = self.mutate(child2)
        b2 = Board(self.size)
        b2.queensPos = child2

        return(b1, b2)


    def mutate(self, child):
        rnd = random.uniform(0, 1)
        if rnd < 0.3:
            pos = random.randint(0, self.size - 1)
            num = random.randint(0, self.size - 1)
            child = list(child)
            child[pos] = num
            child = ''.join(map(str, child))
        return child

    def preserve_bests(self):
        elements = []
        for i in range(len(self.population)):
            elements.append((self.population[i], self.population[i].get_h()))

        elements = sorted(elements, key=itemgetter(1))

        result = []
        for e in elements:
            result.append(e[0])

        return result[0:int(len(result)/5)]

    def kill_them_all(self,new_population):
        elements = []
        for i in range(len(new_population)):
            elements.append((new_population[i], new_population[i].get_h()))

        elements = sorted(elements, key=itemgetter(1))

        result = []
        for e in elements:
            result.append(e[0])
        
        result.reverse()

        return result[int(len(result)/5):]

    def select_best(self,count):
        for i in range(len(self.population)):
            cost = self.population[i].get_h()
            if cost < self.best_fit:
                self.best_fit = cost
                self.best = self.population[i]
                self.best_iteration = count

            if i == 0:
                self.h_to_g.append(cost)




class Board:
    def __init__(self, size):
        self.size = size
        #self.queensPos = [4,5,6,3,4,5,6,5]
        self.queensPos = [n for n in range(0, self.size)]
        random.shuffle(self.queensPos)
        self.queensPos = ''.join(map(str, self.queensPos))



    def get_h(self):
        h = 0
        des_diag = []
        asc_diag = []

        for i in range(self.size):
            elem1 = int(self.queensPos[i]) - i
            des_diag.append(elem1)

            elem2 = int(self.queensPos[i]) + i
            asc_diag.append(elem2)

            for j in range(i+1,self.size,1):
                if self.queensPos[i] == self.queensPos[j]:
                    h +=1

        for i in range(self.size):
            for j in range(i + 1, self.size, 1):
                if des_diag[i] == des_diag[j]:
                    h += 1
                if asc_diag[i] == asc_diag[j]:
                    h += 1
        return h


    def print_board(self):
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
            board[int(self.queensPos[i])][i].value = u"\u2B1B"
            queensNodes.append(board[int(self.queensPos[i])][i])


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
