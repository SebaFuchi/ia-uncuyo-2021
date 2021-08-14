import random
import math

class Environment:
    def __init__(self,sizeX,sizeY,dirt_rate):

        init_posX = random.randint(0,sizeX-1)
        init_posY = random.randint(0,sizeY-1)
        self.table = [[0] * sizeX for i in range(sizeY)]
        self.actX = init_posX
        self.actY = init_posY

        total_dirty_spaces = math.ceil((sizeX*sizeY) * dirt_rate)
        self.dirty_spaces = total_dirty_spaces
        while total_dirty_spaces != 0:
            x = random.randint(0, (sizeX)-1)
            y = random.randint(0, (sizeY)-1)
            if (self.table[x][y] == 0):
                self.table[x][y] = 1
                total_dirty_spaces -= 1


    def is_dirty(self):
        if self.table[self.actX][self.actY] == 1:
            return True
        return False

    def get_performance(self):
        cont = 0
        for i in range(len(self.table)):
            for j in range(len(self.table[i])):
                if (self.table[i][j] == 1):
                    cont += 1
        
        result = 100.0 - ((cont * 100)/self.dirty_spaces)
        print("Porcentaje de suciedad eliminada: " + str(result) + "%")
        print("Espacios sucios generados inicialmente: " + str(self.dirty_spaces))
        print("Espacios sucios restantes: " + str(cont))
        return

    def print_enviroment(self):
        for i in range(len(self.table)):
            print(self.table[i])
            print()
