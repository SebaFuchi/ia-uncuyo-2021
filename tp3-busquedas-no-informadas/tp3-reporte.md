# REPORTE #
 
## PUNTO B ##
 
| |Búsqueda por Anchura| Búsqueda por Profundidad limitada |Busqueda Uniforme|
|---|---|---|---|
|Media Aritmetica|4743.666666666667 | 2598.9444444444443 |4530.866666666667 |
|Desviación Estandar|2859.6523219263654 | 1771.137536500939 |2475.973256684347 |
 
## PUNTO C ##
 
Teniendo en cuenta que la consigna del punto A es la siguiente:
"Implementar un agente basado en objetivos que dado un punto de inicio y un punto destino, encuentre el camino óptimo."
 
#### Búsqueda por Anchura ####
 
Este método se ejecutó sobre un grafo no ponderado, ya que su medida de camino más óptimo, es el camino más cercano o más corto.
 
Este método es más ineficiente que los otros si tenemos en cuenta su complejidad espacial y temporal, ya que revisa mucha mayor cantidad de posibilidades, pero a su vez, de esta forma se asegura de encontrar siempre el camino más óptimo, en su caso, el camino más corto al destino.
 
 
#### Búsqueda por Profundidad limitada ####
 
Para poder aplicar este método se utilizó un grafo ponderado generado de manera aleatoria, ya que no tiene sentido aplicarlo en un grafo no ponderado o del mismo coste, ya que no seguiría ningún criterio para encontrar el camino mas optimo, si no que elegiría caminos aleatorios hasta dar con el objetivo.
 
#### Búsqueda Uniforme ####
 
Este método también se implementó sobre un grafo ponderado, ya que la idea de este método es hacerlo sobre un grafo de este tipo, si no sería exactamente igual que una búsqueda en profundidad sobre un grafo no ponderado.
 
### Conclusión ###
 
Con lo antes explicado, a cada uno de los métodos se los colocó en su "ambiente ideal", puntualmente a la búsqueda en profundidad y a la búsqueda uniforme, ya que se los hizo funcionar en un entorno que simula ser ponderado 
 
Teniendo esto en cuenta, y recordando el objetivo inicial "Implementar un agente basado en objetivos que dado un punto de inicio y un punto destino, encuentre el camino óptimo.", el método más óptimo para un grafo no ponderado es la búsqueda en amplitud, ya que aplicar alguno de los otros dos métodos en un grafo de estas características no tendría sentido.
 
Si se trata de un grafo ponderado, aplicar búsqueda por amplitud no tendría sentido ya que revisaria un nivel a la vez hasta encontrar el destino, pero revisaria muchos nodos de más ya que su principal ventaja se da en grafos no ponderados, en los cuales no hay un criterio de búsqueda definido. Al ser un grafo en el cual los caminos tiene peso, el método más adecuado para encontrar el camino óptimo sería la búsqueda uniforme, ya que puede que revise más cantidad de nodos, pero por su funcionamiento, siempre continúa su ramificación por el camino que menos peso tiene, actualizando estos datos ordenando la lista de nodos descubiertos en función de su peso, de esta forma se asegura de elegir el camino mas optimo.
La busqueda en profundidad, encontrara el camino de forma mas rapida y revisando menos nodos, pero no sera el mas optimo probablemente, ya que al desencolar de una lista normal, elige un nodo nuevo de los últimos que descubrió, no teniendo en cuenta el contexto general de cual de TODOS los descubiertos tiene el menor peso, por esto es más rápido pero no da el objetivo deseado.
 
Por esto, para grafos no ponderados, la opción siempre sera búsqueda en amplitud, y en grafos ponderados, el camino mas optimo será dado por la búsqueda uniforme, por lo que este seria el mas apropiado para este ejercicio, otra vez, si utilizamos un grafo no ponderado.
