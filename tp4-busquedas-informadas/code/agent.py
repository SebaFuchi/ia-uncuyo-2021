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