# REPORTE #
 
## PUNTO B ##
 
| |Búsqueda por Anchura| Búsqueda por Profundidad limitada |Busqueda Uniforme|
|---|---|---|---|
|Media Aritmetica|4743.666666666667 | 64.43333333333334 |66.33333333333333 |
|Desviación Estandar|2859.6523219263654 | 32.39804520852042 |36.93734987911225 |
 
## PUNTO C ##
 
Teniendo en cuenta que la consigna del punto A es la siguiente:
"Implementar un agente basado en objetivos que dado un punto de inicio y un punto destino, encuentre el camino óptimo."
 
#### Búsqueda por Anchura ####
 
Este método es mucho más ineficiente que los otros dos si se considera tanto su complejidad temporal como espacial, ya que revisa mucha mayor cantidad de puntos en el tablero, pero haciendo esto, podemos estar 100% seguros de que el camino que encontró es el óptimo. Sumado a esto, el ejercicio que se plantea se trata de encontrar el camino mas optimo pero en una grilla no ponderada, por lo que el método de búsqueda por amplitud, sirve especialmente para estos casos ya que, como antes mencione, si o si encontrara el camino mas optimo, si es que existe un camino posible.
 
#### Búsqueda por Profundidad limitada ####
 
Con una implementación estándar de este método, no es posible encontrar el camino más óptimo, ya que el tablero no es ponderado, por lo que el algoritmo no puede decidir qué camino le conviene basándose en los pesos de los posibles caminos. Para mejorar su eficiencia, implemente una pseudo ponderación, la cual consiste en lo siguiente:
 
Una vez que se descubren nuevos nodos, a estos se los ordena en la lista a revisar según su distancia al punto destino, de esta forma, los más cercanos serán desencolados y revisados primero. De esta manera logre mejorar considerablemente el proceso, pero igualmente no se puede asegurar que con esta modificación encontrará siempre el camino óptimo, debido a los obstáculos.
 
Sin esta modificación, el algoritmo de búsqueda en profundidad limitada, tomaría caminos de manera aleatoria, ya que todos los caminos tendrían el mismo costo, hasta encontrar el destino o alcanzar el límite de profundidad especificado.
 
#### Búsqueda Uniforme ####
 
Con este método, pasa lo mismo que con la búsqueda en profundidad, están planteados para ser eficientes si se utiliza un grafo ponderado, pero no es el caso de este ejercicio.
 
De igual manera, para mejorar su eficiencia, utilice la estrategia de "pseudo ponderar" en función de la distancia al destino. De esta forma, puedo sacar el juego a la idea de este método, actualizando el orden de su lista de prioridad en función de la distancia que tiene cada nuevo punto descubierto con respecto al destino. Si no se aplica esta modificación, no tendría sentido implementar este método, ya que funciona exactamente igual que la búsqueda en profundidad, elegiría caminos de forma aleatoria hasta dar con el resultado. 
Si pasara eso, no estaríamos obteniendo el mejor camino
 
### Conclusión ###
 
Teniendo en cuenta la consigna de buscar el mejor camino, con las modificaciones que aplique a la búsqueda en profundidad y la búsqueda uniforme, estos serían los más eficientes ya que se estaría simulando un entorno ponderado y así logran su eficiencia.
 
Pero si se dejan de lado estas modificaciones, osea se trabajara con los métodos en su forma estándar, teniendo en cuenta que los estamos aplicando en un grafo no ponderado, nunca lograron encontrar el camino mas optimo al destino.
 
En conclusión, si nos limitamos a la consigna de "Implementar un agente basado en objetivos que dado un punto de inicio y un punto destino, encuentre el camino óptimo.", el método más adecuado para resolver esta tarea sería la búsqueda en amplitud, ya que todas las veces encontrara el camino mas optimo al destino.
