import hill_climbing
import simulated_annealing
import genetic


# c = hill_climbing.Climber(8)
# c.solution_finder()

#s = simulated_annealing.Climber(8)
#s.solution_finder()

g = genetic.Genetic(8)

best = g.solution_finder()

print("BEST")
best.print_board()
print(best.get_h())
print(g.best_iteration)
