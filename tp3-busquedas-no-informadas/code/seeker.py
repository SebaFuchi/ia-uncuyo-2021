import random

class Seeker:
    def breadth_first_search(self, agnt, env):
        startNode = env.startNode
        finalNode = env.endNode
        frontier = [(startNode, "I")]
        explored = []
        
        result = self.breadth_first_searchR(env, agnt, frontier, explored, finalNode)

        if result != None:
            return result
        return False
        

    def breadth_first_searchR(self, env, agnt, frontier, explored, finalNode):

        while len(frontier) > 0:
            actNode = frontier.pop(0)
            explored.append(actNode)

            if self.test_path(agnt,actNode[1], finalNode) == True:
                agnt.env.actX = agnt.env.startX
                agnt.env.actY = agnt.env.startY
                return actNode[1]
            else:
                agnt.env.actX = agnt.env.startX
                agnt.env.actY = agnt.env.startY

            self.get_valid_nodes(env, frontier, explored, actNode)

        return None


    def test_path(self, agnt, path, destiny):
        while len(path) > 0:    
            action = path[0]
            path = path[1:len(path)]
            agnt.act(action)
            x = agnt.env.table[agnt.env.actY][agnt.env.actX]

        if x == destiny:
            return True
        return False
            
    
    def get_valid_nodes(self, env, frontier, explored, actNode):

        tempList = []
        tempExp = []

        for element in explored:
            tempExp.append(element[0])

        if ((actNode[0].x - 1 >= 0) and (env.table[actNode[0].y][actNode[0].x - 1].value != u"\u2B1B")):
            if (env.table[actNode[0].y][actNode[0].x - 1] not in tempExp) == True:
                tempList.append((env.table[actNode[0].y][actNode[0].x - 1], actNode[1]+"L"))

        if ((actNode[0].x + 1 < env.size) and (env.table[actNode[0].y][actNode[0].x + 1].value != u"\u2B1B")):
            if (env.table[actNode[0].y][actNode[0].x + 1] not in tempExp) == True:
                tempList.append((env.table[actNode[0].y][actNode[0].x + 1], actNode[1]+"R"))

        if ((actNode[0].y - 1 >= 0) and (env.table[actNode[0].y - 1][actNode[0].x].value != u"\u2B1B")):
            if (env.table[actNode[0].y - 1][actNode[0].x] not in tempExp) == True:
                tempList.append((env.table[actNode[0].y - 1][actNode[0].x], actNode[1]+"U"))

        if ((actNode[0].y + 1 < env.size) and (env.table[actNode[0].y + 1][actNode[0].x].value != u"\u2B1B")):
            if (env.table[actNode[0].y + 1][actNode[0].x] not in tempExp) == True:
                tempList.append((env.table[actNode[0].y + 1][actNode[0].x], actNode[1]+"D"))

        random.shuffle(tempList)
        frontier.extend(tempList)
        return
