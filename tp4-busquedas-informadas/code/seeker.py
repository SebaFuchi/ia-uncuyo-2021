import math
from operator import itemgetter
import time

class Seeker:

    def a_star_search(self, env):
        frontier = [(env.startNode, "I")]
        explored = []
        cost = 0

        result = self.a_star_searchR(env, frontier, explored, cost)

        if result != None:
            return result
        return False

    def a_star_searchR(self, env, frontier, explored, prevCost):

        destiny = env.endNode
        while len(frontier) > 0:
            actNode = frontier.pop(0)

            # PATH TRACKER
            # time.sleep(0.5)
            # env. print_enviroment()
            # print("")

            # EXPLORED
            # if actNode[0].value == u"\U0001F7E8":
            #     actNode[0].value = u"\U0001F7EA"
            explored.append(actNode)

            if actNode[0] == env.endNode:
                return (actNode[1], explored)

            prevCost += 1
            result = self.get_valid_nodes(env, explored, frontier, actNode)
            ## DISCOVERED
            # for element in result:
            #     if element[0].value == u"\u2B1C":
            #         element[0].value = u"\U0001F7E8"
            frontier.extend(result)

            frontier = self.point_organizer(frontier, destiny, prevCost)
        return None

    def point_organizer(self, list, destiny, prevCost):

        emptyList = []

        for element in list:
            res = math.sqrt((element[0].x-destiny.x) **
                            2 + (element[0].y-destiny.y)**2)
            obj = (element, (1 + prevCost) + res)
            emptyList.append(obj)
        emptyList = sorted(emptyList, key=itemgetter(1))

        restList = []

        for element in emptyList:
            restList.append(element[0])

        return restList


    def a_star_search_ponder(self, env):
        frontier = [(env.startNode, "I")]
        explored = []
        cost = 0

        result = self.a_star_search_ponderR(env, frontier, explored, cost)

        if result != None:
            return result
        return False

    def a_star_search_ponderR(self, env, frontier, explored, prevCost):

        destiny = env.endNode
        while len(frontier) > 0:
            actNode = frontier.pop(0)

            # PATH TRACKER
            # time.sleep(0.5)
            # env. print_enviroment()
            # print("")

            # EXPLORED
            # if actNode[0].value == u"\U0001F7E8":
            #     actNode[0].value = u"\U0001F7EA"
            explored.append(actNode)

            if actNode[0] == env.endNode:
                return (actNode[1], explored)

            prevCost += actNode[0].cost
            result = self.get_valid_nodes(env, explored, frontier, actNode)
            ## DISCOVERED
            # for element in result:
            #     if element[0].value == u"\u2B1C":
            #         element[0].value = u"\U0001F7E8"
            frontier.extend(result)

            frontier = self.point_organizer_ponder(frontier, destiny, prevCost)
        return None

    def point_organizer_ponder(self, list, destiny, prevCost):

        emptyList = []

        for element in list:
            res = math.sqrt((element[0].x-destiny.x) **
                            2 + (element[0].y-destiny.y)**2)
            obj = (element, (element[0].cost + prevCost) + res)
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
                    tempList.append(
                        (env.table[actNode[0].y][actNode[0].x - 1], actNode[1]+"L"))

        if ((actNode[0].x + 1 < env.size) and (env.table[actNode[0].y][actNode[0].x + 1].value != u"\u2B1B")):
            if (env.table[actNode[0].y][actNode[0].x + 1] not in tempExp) == True:
                if (env.table[actNode[0].y][actNode[0].x + 1] not in tempFron) == True:
                    tempList.append(
                        (env.table[actNode[0].y][actNode[0].x + 1], actNode[1]+"R"))

        if ((actNode[0].y - 1 >= 0) and (env.table[actNode[0].y - 1][actNode[0].x].value != u"\u2B1B")):
            if (env.table[actNode[0].y - 1][actNode[0].x] not in tempExp) == True:
                if (env.table[actNode[0].y - 1][actNode[0].x] not in tempFron) == True:
                    tempList.append(
                        (env.table[actNode[0].y - 1][actNode[0].x], actNode[1]+"U"))

        if ((actNode[0].y + 1 < env.size) and (env.table[actNode[0].y + 1][actNode[0].x].value != u"\u2B1B")):
            if (env.table[actNode[0].y + 1][actNode[0].x] not in tempExp) == True:
                if (env.table[actNode[0].y + 1][actNode[0].x] not in tempFron) == True:
                    tempList.append(
                        (env.table[actNode[0].y + 1][actNode[0].x], actNode[1]+"D"))
        return tempList
