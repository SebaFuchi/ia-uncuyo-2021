import math
from treeNodes import *

class DecisionTree:
    def __init__(self, dataset, atributes):
        self.dataset = dataset
        self.atributes = atributes
        self.calcAtributes()

    def calcAtributes(self):
        pos = 0
        neg = 0
        last = len(self.dataset[0]) - 1
        for i in range(len(self.dataset)):
            res = self.dataset[i][last]
            if res == "yes":
                pos += 1
            else:
                neg += 1

        Imp_g = self.impForm(pos/(pos+neg), neg/(pos+neg))
        attrib_L = []
        att_ops = []
        att_num = 0
        for att in self.atributes:
            if att != "play":
                explored = []
                for i in range(len(self.dataset)):
                    ds_val = self.dataset[i][att_num]
                    ds_res = self.dataset[i][last]
                    attVal = None
                    for v in explored:
                        if v.name == ds_val:
                            attVal = v
                            break

                    if attVal == None:
                        attVal = AtVal()
                        attVal.name = ds_val
                        if ds_val not in att_ops:
                            att_ops.append(ds_val)

                        if ds_res == "yes":
                            attVal.posibleValues += 1
                        else:
                            attVal.negativeValues += 1
                        explored.append(attVal)
                    else:
                        if ds_res == "yes":
                            attVal.posibleValues += 1
                        else:
                            attVal.negativeValues += 1

                acum = 0
                for v in explored:
                    neg_pos = v.posibleValues + v.negativeValues
                    acum += (neg_pos / (pos + neg)) * self.impForm(v.posibleValues / neg_pos, v.negativeValues / neg_pos)

                at = Atribute()
                at.values = att_ops
                att_ops = []
                at.gain = Imp_g - acum
                at.name = att
                at.number = att_num
                att_num += 1
                attrib_L.append(at)
                explored = []
            self.att_L = attrib_L

    def impForm(self, ft, st):
        fT = 0
        sT = 0
        if ft > 0:
            fT = - ft * math.log(ft, 2)
        if st > 0:
            sT =  st * math.log(st, 2)

        return fT - sT

    def treeLeanring(self, examples,atributes, def_val):
        if len(examples) == 0:
            return def_val
        else:
            last = len(examples[0]) - 1
            pos = 0
            neg = 0
            for i in range(len(examples)):
                res = examples[i][last]
                if res == "yes":
                    pos += 1
                else:
                    neg += 1
            
            if len(examples) == pos:
                return "yes"
            elif len(examples) == neg:
                return "no"
            else:
                if len(atributes) == 0:
                    if pos > neg:
                        return "yes"
                    else:
                        return "no"
                else:
                    atrib = atributes[0]
                    for att in atributes:
                        if att.gain > atrib.gain:
                            atrib = att
                    atributes.remove(atrib)
                    node = Node()
                    node.value = atrib.name
                    node.childrens = []
                    m = None
                    if pos > neg:
                        m = "yes"
                    else:
                        m = "no"

                    explored = []
                    for i in range(len(examples)):
                        ds_val = self.dataset[i][atrib.number]
                        ds_res = self.dataset[i][last]
                        attVal = None
                        for v in explored:
                            if v == ds_val:
                                attVal = v
                                break

                        if attVal == None:
                            explored.append(ds_val)
                    
                    for op in explored:
                        ex_op = []
                        for i in range(len(examples)):
                            if examples[i][atrib.number] == op:
                                ex_op.append(examples[i])
                        r = ex_op
                        attrL = self.att_L
                        subT = self.treeLeanring(r, attrL, m)
                        subN = SubTree()
                        subN.label = op
                        subN.value = subT
                        node.childrens.append(subN)

                    return node




