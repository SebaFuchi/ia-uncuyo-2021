import math
from operator import itemgetter


class Seeker:
    def breadth_first_search(self, env):
        frontier = [(env.startNode, "I")]
        explored = []

        result = self.breadth_first_searchR(env, frontier, explored)

        if result != None:
            return result
        return False

    def breadth_first_searchR(self, env, frontier, explored):

        while len(frontier) > 0:
            actNode = frontier.pop(0)
            explored.append(actNode)

            if actNode[0] == env.endNode:
                return actNode[1]

            result = self.get_valid_nodes(env, explored, actNode)
            frontier.extend(result)
        return None

    def get_valid_nodes(self, env, explored, actNode):

        tempList = []
        tempExp = []

        for element in explored:
            tempExp.append(element[0])

        if ((actNode[0].x - 1 >= 0) and (env.table[actNode[0].y][actNode[0].x - 1].value != u"\u2B1B")):
            if (env.table[actNode[0].y][actNode[0].x - 1] not in tempExp) == True:
                tempList.append(
                    (env.table[actNode[0].y][actNode[0].x - 1], actNode[1]+"L"))

        if ((actNode[0].x + 1 < env.size) and (env.table[actNode[0].y][actNode[0].x + 1].value != u"\u2B1B")):
            if (env.table[actNode[0].y][actNode[0].x + 1] not in tempExp) == True:
                tempList.append(
                    (env.table[actNode[0].y][actNode[0].x + 1], actNode[1]+"R"))

        if ((actNode[0].y - 1 >= 0) and (env.table[actNode[0].y - 1][actNode[0].x].value != u"\u2B1B")):
            if (env.table[actNode[0].y - 1][actNode[0].x] not in tempExp) == True:
                tempList.append(
                    (env.table[actNode[0].y - 1][actNode[0].x], actNode[1]+"U"))

        if ((actNode[0].y + 1 < env.size) and (env.table[actNode[0].y + 1][actNode[0].x].value != u"\u2B1B")):
            if (env.table[actNode[0].y + 1][actNode[0].x] not in tempExp) == True:
                tempList.append(
                    (env.table[actNode[0].y + 1][actNode[0].x], actNode[1]+"D"))

        tempList = self.point_organizer(tempList, env.endNode)
        return tempList

    def depth_first_search(self, env):
        firstNode = (env.startNode, "I")
        explored = []

        result = self.depth_first_searchR(env, firstNode, explored, env.size*2)
        if result != None:
            return result
        return False


    def depth_first_searchR(self, env, actNode, explored, limit):
        if limit > 0:
            explored.append(actNode)

            if actNode[0] == env.endNode:
                return actNode[1]

            result = self.get_valid_nodes(env, explored, actNode)

            while len(result) > 0:
                node = result.pop(0)
                res = self.depth_first_searchR(env, node, explored, limit - 1)
                if res != None:
                    return res
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
