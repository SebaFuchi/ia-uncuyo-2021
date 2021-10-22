import fowardchecking
import backtraking
import matplotlib.pyplot as plt


cant_queens = [4,8,10,12,15]

time_foward= []
states_foward = []
for i in cant_queens:
    b = fowardchecking.Foward(i)
    result = b.find_solution()
    states_foward.append(result[1])
    time_foward.append(result[2])
print(states_foward)
print(time_foward)

fig, ax = plt.subplots()
ax.boxplot(states_foward)
plt.show()
