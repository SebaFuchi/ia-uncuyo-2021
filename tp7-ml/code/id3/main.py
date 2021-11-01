import csv
import decisionTree

file = open('tennis.csv')
csvreader = csv.reader(file)
header = next(csvreader)
rows = []
for row in csvreader:
    rows.append(row)
file.close()

dt = decisionTree.DecisionTree(rows, header)
tree = dt.treeLeanring(rows, dt.att_L ,"no")
print(tree)