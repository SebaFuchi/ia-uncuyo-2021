import random

class Agent:
    def __init__(self,env):
        self.env = env
        self.actions = 1000

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

    def idle(self):
        self.actions -= 1
        return 

    def suck(self):
        self.env.table[self.env.actY][self.env.actX] = 0
        self.actions -= 1
        return
    
    def perspective(self):
        if (self.env.table[self.env.actY][self.env.actX] == 1):
            self.suck(self)
        else:
            self.idle(self)
        return
        
    def think(self):
        while self.actions > 0:
            actions = [self.up, self.down, self.left, self.right]
            rand = random.randint(0,3)
            actions[rand](self)
            self.actions -= 1
            self.perspective(self)
        return
