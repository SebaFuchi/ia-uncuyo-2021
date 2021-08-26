import math
from operator import itemgetter

class Seeker:

    def uniform_cost_search(self, env):
        frontier = [(env.startNode, "I")]
        explored = []

        result = self.uniform_cost_searchR(env, frontier, explored)

        if result != None:
            return result
        return False

    def uniform_cost_searchR(self, env, frontier, explored):

        while len(frontier) > 0:
            actNode = frontier.pop(0)
            explored.append(actNode)

            if actNode[0] == env.endNode:
                return (actNode[1], explored)

            result = self.get_valid_nodes(env, explored, frontier, actNode)
            frontier.extend(result)

            frontier = self.point_cost_organizer(frontier)
        return None

    def point_organizer(self, list, destiny):
        emptyList = []

        for element in list:
            res = math.sqrt((element[0].x-destiny.x)**2 + (element[0].y-destiny.y)**2)
            obj = (element, res)
            emptyList.append(obj)
        emptyList = sorted(emptyList, key=itemgetter(1))

        restList = []

        for element in emptyList:
            restList.append(element[0])

        return restList

    def get_valid_nodes(self, env, explored, frontier, actNode):

        tempList = []
        tempExp = []
        tempFron = []

        for element in explored:
            tempExp.append(element[0])

        for element in frontier:
            tempFron.append(element[0])

        if ((actNode[0].x - 1 >= 0) and (env.table[actNode[0].y][actNode[0].x - 1].value != u"\u2B1B")):
            if (env.table[actNode[0].y][actNode[0].x - 1] not in tempExp) == True:
                if (env.table[actNode[0].y][actNode[0].x - 1] not in tempFron) == True:
                    tempList.append((env.table[actNode[0].y][actNode[0].x - 1], actNode[1]+"L"))

        if ((actNode[0].x + 1 < env.size) and (env.table[actNode[0].y][actNode[0].x + 1].value != u"\u2B1B")):
            if (env.table[actNode[0].y][actNode[0].x + 1] not in tempExp) == True:
                if (env.table[actNode[0].y][actNode[0].x + 1] not in tempFron) == True:
                    tempList.append((env.table[actNode[0].y][actNode[0].x + 1], actNode[1]+"R"))

        if ((actNode[0].y - 1 >= 0) and (env.table[actNode[0].y - 1][actNode[0].x].value != u"\u2B1B")):
            if (env.table[actNode[0].y - 1][actNode[0].x] not in tempExp) == True:
                if (env.table[actNode[0].y - 1][actNode[0].x] not in tempFron) == True:
                    tempList.append((env.table[actNode[0].y - 1][actNode[0].x], actNode[1]+"U"))

        if ((actNode[0].y + 1 < env.size) and (env.table[actNode[0].y + 1][actNode[0].x].value != u"\u2B1B")):
            if (env.table[actNode[0].y + 1][actNode[0].x] not in tempExp) == True:
                if (env.table[actNode[0].y + 1][actNode[0].x] not in tempFron) == True:
                    tempList.append((env.table[actNode[0].y + 1][actNode[0].x], actNode[1]+"D"))
        return tempList