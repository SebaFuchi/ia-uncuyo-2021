import seeker
import time
import environment
import math

class Agent:
    def __init__(self):
        self.serch = seeker.Seeker()

    def idle(self):
        return 

    def up(self):
        if (self.env.actY - 1 >= 0):
            self.env.actY -= 1
        return

    def down(self):
        if (self.env.actY + 1 < len(self.env.table)):
            self.env.actY += 1
        return

    def left(self):
        if (self.env.actX - 1 >= 0):
            self.env.actX -= 1
        return

    def right(self):
        if (self.env.actX + 1 < len(self.env.table[0])):
            self.env.actX += 1
        return

    def act(self, action):
        if action == "I":
            self.idle()
            return
        if action == "U":
            self.up()
            return
        if action == "D":
            self.down()
            return
        if action == "L":
            self.left()
            return
        
        self.right()
        return

    def seekAS(self):
        cantNodos = []
        vueltas = 30
        for i in range(30):
            self.env = environment.Environment()
            print("")
            print("START "+str(i) + " MAP")
            self.env.print_enviroment()
            start = time.time()
            path = self.serch.a_star_search(self.env)
            if path == False:
                print("")
                print("can't be solved")
                print("")
                vueltas -= 1
                continue
            
            cantNodos.append(len(path[1]))
            moves = path[0]
            self.paint_path(path[0])
            print("------")
            print("SOLVED")
            self.env.print_enviroment()
            end = time.time()
            print("")
            print("Time: "+str(end-start))
            print("Path: " + moves[1:])
            print("")
        
        cont = 0
        for nodos in cantNodos:
            cont += nodos

        media = cont/vueltas

        cont = 0
        for nodos in cantNodos:
            cont += (nodos - media)**2

        desv = math.sqrt(cont/(len(cantNodos)-1))

        print("RESULTADOS:")
        print("------------")
        print("MEDIA: " + str(media))
        print("DESVIACION ESTANDAR: " + str(desv))

    def seekASP(self):
        cantNodos = []
        vueltas = 30
        for i in range(30):
            self.env = environment.Environment()
            print("")
            print("START "+str(i) + " MAP")
            self.env.print_enviroment()
            start = time.time()
            path = self.serch.a_star_search_ponder(self.env)
            if path == False:
                print("")
                print("can't be solved")
                print("")
                vueltas -= 1
                continue
            
            cantNodos.append(len(path[1]))
            moves = path[0]
            self.paint_path(path[0])
            print("------")
            print("SOLVED")
            self.env.print_enviroment()
            end = time.time()
            print("")
            print("Time: "+str(end-start))
            print("Path: " + moves[1:])
            print("")
        
        cont = 0
        for nodos in cantNodos:
            cont += nodos

        media = cont/vueltas

        cont = 0
        for nodos in cantNodos:
            cont += (nodos - media)**2

        desv = math.sqrt(cont/(len(cantNodos)-1))

        print("RESULTADOS:")
        print("------------")
        print("MEDIA: " + str(media))
        print("DESVIACION ESTANDAR: " + str(desv))

    

    def paint_path(self, path):
        while len(path) > 0:    
            action = path[0]
            path = path[1:len(path)]
            if action == "I" or len(path) == 0:
                self.act(action)
            else:
                self.act(action)
                self.env.table[self.env.actY][self.env.actX].value = u"\U0001F7E6"
        return