import agent

ag = agent.Agent()

## Si se descomententan los diferentes metodos, se ejecutaran 30 caminos aleatorios resueltos(si es posible) por dicho metodo, 
# ademas se mostrara la media aritmetica y la desviacion estandar de dichos casos

## depth_firs
#ag.seekDF()

## breadth_first
ag.seekBF()

## uniform_cost
#ag.seekUC()

