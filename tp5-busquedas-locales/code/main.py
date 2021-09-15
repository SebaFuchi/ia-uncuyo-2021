import hill_climbing
import simulated_annealing
import genetic
import math

flag = False
h_to_g = []
opt_result = 0
prev_states = []
time = []
cont = 0
iter = 30
for i in range(iter):
    #c = hill_climbing.Climber(8)
    #c = simulated_annealing.Climber(8)
    c= genetic.Genetic(10)
    s = c.solution()
    if s[0] == 0:
        cont += 1
        opt_result += 1
        prev_states.append(s[1])
        time.append(s[2])
        if flag == False:
            h_to_g = s[3]
            flag = True
    
if cont != 0:
    print()
    print("CANTIDAD DE SOLUCIONES ENCONTRADAS:")
    print(cont)
    porc_opt_result = opt_result/iter
    print()
    print("PORCENTAJE DE VECES QUE SE LLEGA A UNA SOLUCION OPTIMA: ")
    print(porc_opt_result)
    print()
    ## TIEMPO
    c = 0
    for t in time:
        c += t
    media_t = c/cont
    print("TIEMPO DE EJECUCION PROMEDIO PARA ALCANZAR UNA SOLUCION OPTIMA: ")
    print(media_t)
    print()
    c = 0
    for t in time:
        c += (t - media_t)**2
    desv_t = math.sqrt(c/(len(time)))
    print("DESVIACION ESTANDAR DEL TIEMPO PARA ENCONTRAR UNA SOLUCION OPTIMA: ")
    print(desv_t)
    print()
    ## ESTADOS
    c = 0
    for s in prev_states:
        c += s
    media_s = c/cont
    print("MEDIA DE ESTADOS NECESARIOS PARA ALCANZAR UNA SOLUCION OPTIMA: ")
    print(media_s)
    print()
    c = 0   
    for s in prev_states:
        c += (s - media_s)**2
    desv_s = math.sqrt(c/(len(prev_states)))
    print("DESVIACION ESTANDAR DE LOS ESTADOS PARA ENCONTRAR UNA SOLUCION OPTIMA: ")
    print(desv_s)
    print()
else:
    print("Nunca encontro solucion")

#print(h_to_g)
print(prev_states)
print(time)


# g = genetic.Genetic(8)

# best = g.solution_finder()

# print("BEST")
# best.print_board()
# print(best.get_h())
# print(g.best_iteration)
