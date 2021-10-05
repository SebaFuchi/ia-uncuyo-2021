#### 1. Describir en detalle una formulación CSP para el Sudoku.
	
Una vez construido el tablero y distribuido los respectivos valores de forma aleatoria, elegiremos una celda vacía de forma aleatoria.
Después de esto, se debe proceder a checkear sus 3 correspondientes unidades, la fila en la que está, la columna y el bloque de 3x3.
Para encontrar la solución, se revisa una a una las unidades, de esta forma, se van descubriendo que valores ya fueron utilizados y estos valores se eliminan del dominio de la casilla que está siendo evaluada. Si el dominio de la casilla queda con un solo valor posible, se asigna dicho valor a esta casilla, de no poder continuar eliminando valores y la longitud del dominio no es igual a 1, pasaría a otra casilla vacía a aplicar el mismo procedimiento de evaluación. De esta forma, se irían descubriendo los valores de cada casillero hasta completar el tablero, no buscando cuales sí pueden funcionar, si no eliminando los que sabemos que no podemos utilizar.


#### 2. Utilizar el algoritmo AC-3 para demostrar que la arco consistencia puede detectar la inconsistencia de la asignación parcial {WA=red, V=blue} para el problema del colorar el mapa de Australia (Figura 5.1 AIMA 2da edición ).

Primero aplico las asignaciones de la consigna:
La cola inicialmente está compuesta por todos los arcos.

queue= {(WA,NT),(WA,SA),(NT,WA),(NT,SA),(NT,Q),(SA,WA),(SA,NT),(SA,Q),(SA,NSW),(SA,V),
(Q,NT),(Q,SA),(Q,NSW),(NSW,Q),(NSW,SA),(NSW,V),(V,SA),(V,NSW)}

El dominio de cada variable es el siguiente:
WA = {rojo}
NT = {rojo,verde,azul}
SA = {rojo,verde,azul}
Q = {rojo,verde,azul}
NSW = {rojo,verde,azul}
T = {rojo,verde,azul}
V = {azul}


Luego, elijo el arco WA-NT para verificar su consistencia, sacándolo de la cola. 
Al hacer la verificación, encuentro que WA es arco-consistente con NT, por lo que se pasa al siguiente arco.
El nuevo arco es WA-SA, el cual también es arco-consistente.

El próximo arco, NT-WA no es arco consistente, solucionamos esto eliminando el color rojo del dominio de NT. Luego de eliminar esto, se deben revisar los vecinos de NT, por lo que se agregan a la cola los arcos WA-NT, SA-NT y Q-NT (estas dos últimas ya pertenecían a la cola por lo que no serán agregadas).

queue actual = {(NT,SA),(NT,Q),(SA,WA),(SA,NT),(SA,Q),(SA,NSW),(SA,V),
(Q,NT),(Q,SA),(Q,NSW),(NSW,Q),(NSW,SA),(NSW,V),(V,SA),(V,NSW),(WA,NT)}

Tanto el arco NT-SA y NT-Q son arco consistentes.

El sigte arco es SA-WA, el cual no es arco-consistente.Se soluciona eliminando rojo del dominio de SA. Luego de esto, los arcos a los vecinos de SA a la cola((WA,SA),(NT,SA))

queue = {(SA,NT),(SA,Q),(SA,NSW),(SA,V),(Q,NT),(Q,SA),(Q,NSW),(NSW,Q),(NSW,SA),(NSW,V),
(V,SA),(V,NSW),(WA,NT),(WA,SA),(NT,SA)}
Dominios:
WA = {rojo}
NT = {verde,azul}
SA = {verde,azul}
Q = {rojo,verde,azul}
NSW = {rojo,verde,azul}
T = {rojo,verde,azul}
V = {azul}

(SA,NT),(SA,Q),(SA,NSW) son arco consistentes.

SA-V no es arco consistente, lo soluciono eliminando azul del dominio de SA y luego agrego los arcos de sus vecinos a la cola.

queue = {(Q,NT),(Q,SA),(Q,NSW),(NSW,Q),(NSW,SA),(NSW,V),(V,SA),(V,NSW),(WA,NT),(WA,SA),
(NT,SA)}

Dominios: 
WA = {rojo}
NT = {verde,azul}
SA = {verde}
Q = {rojo,verde,azul}
NSW = {rojo,verde,azul}
T = {rojo,verde,azul}
V = {azul}
Q-NT es arco-consistente.
Q-SA no es arco consistente, soluciono eliminando verde del dominio de Q y agregó sus vecinos a la cola.

queue = {(Q,NSW),(NSW,Q),(NSW,SA),(NSW,V),(V,SA),(V,NSW),(WA,NT),(WA,SA),
(NT,SA),(NT,Q),(SA,Q)}

Dominios: 
WA = {rojo}
NT = {verde,azul}
SA = {verde}
Q = {rojo,azul}
NSW = {rojo,verde,azul}
T = {rojo,verde,azul}
V = {azul}

Q-NSW, NSW-Q son arco-consistentes.

NSW-SA no es arco-consistente, solución: eliminar verde de NSW y luego agrego los arcos de sus vecinos a la cola.

queue = {(NSW,V),(V,SA),(V,NSW),(WA,NT),(WA,SA),
(NT,SA),(NT,Q),(SA,Q),(Q,NSW),(SA,NSW)}

Dominios: 
WA = {rojo}
NT = {verde,azul}
SA = {verde}
Q = {rojo,azul}
NSW = {rojo,azul}
T = {rojo,verde,azul}
V = {azul}

NSW-V no es arco consistente, solución: elimino azul de NSW y agrego los arcos de sus vecinos a la cola.

queue = {(V,SA),(V,NSW),(WA,NT),(WA,SA),
(NT,SA),(NT,Q),(SA,Q),(Q,NSW),(SA,NSW)}

Dominios: 
WA = {rojo}
NT = {verde,azul}
SA = {verde}
Q = {rojo,azul}
NSW = {rojo}
T = {rojo,verde,azul}
V = {azul}

V-SA, V-NSW, WA-NT, WA-SA, NT-SA, NT-Q, SA-Q son arco consistentes.

Q-NSW no es arco consistente, solucion: elimino rojo de Q y agrego los arcos de sus vecinos a la cola.

queue = {(SA,NSW),(NT,Q),(SA,Q),(NSW,Q)}

Dominios: 
WA = {rojo}
NT = {verde,azul}
SA = {verde}
Q = {azul}
NSW = {rojo}
T = {rojo,verde,azul}
V = {azul}

SA-NSW es arco-consistente

NT-Q no es arco consistente, solucion: eliminar azul de NT y agregar los arcos de sus vecinos a la cola.

queue = {(SA,Q),(NSW,Q),(WA,NT),(SA,NT),(Q,NT)}

Dominios: 
WA = {rojo}
NT = {verde}
SA = {verde}
Q = {azul}
NSW = {rojo}
T = {rojo,verde,azul}
V = {azul}

SA-Q, NSW-Q, WA-NT son arco consistentes.

SA-NT no son concistentes, solucion: eliminar verde de SA y agregar los arcos de los vecinos a la cola.
Luego de hacer esto, el dominio de SA = {}, por lo que se llega a un fallo.
De esta manera se demuestra que la asignación parcial  {WA=red, V=blue} llega a un fallo.

#### 3. Cuál es la complejidad en el peor caso cuando se ejecuta AC-3 en un árbol estructurado CSP. (i.e. Cuando el grafo de restricciones forma un árbol: cualquiera dos variables están relacionadas por a lo sumo un camino).

Si se toma una estructura de árbol, en la cual los nodos tengan un padre y no existan ciclos, el peor caso de la complejidad es de O(n(d^2)) .
Esto se logra aplicando la estructura y realizando dos recorridos, primero uno desde las hojas a la raíz y luego haciendo una verificación desde la raíz hasta las hojas. De esta forma, puedo asegurarme de encontrar valores legales ya que al con estas dos pasadas, si existe una solución posible, nos aseguraremos de que los nodos serán arco-consistentes entre sí.

Siendo d el dominio más grande y n el número de aristas del árbol.

#### 4. AC-3 coloca de nuevo en la cola todo arco ( Xk, Xi) cuando cualquier valor es removido del dominio de Xi incluso si cada valor de Xk es consistente con los valores restantes de Xi. Si por cada arco ( Xk,Xi) se lleva cuenta del número de valores que quedan de Xi que sean consistentes con Xk . Explicar como actualizar ese número de manera eficiente y demostrar que la arco consistencia puede lograrse en un tiempo total O(n2d2 )
Se podría implementar que el nodo Xi llevará una lista de los nodos que ya son consistentes con él, inicialmente empezaría vacía. Cuando aseguramos que un nodo Xk es consistente, lo agregamos a esta lista, de esta manera, cuando se remueve un elemento del dominio de Xi, en vez de incorporar a la cola todos los arcos, revisando esta lista, podríamos incorporar sólo los vecinos que no estén en ella (debido a que no aseguramos aún su consistencia) .
Luego, la complejidad del arco consistencia se puede analizar de la siguiente forma:
Un problema tiene a lo sumo O(n^2), siendo n el número de variables, cada arco (Xi,Xk) puede incorporarse en la cola a lo máximo d veces,(d es el dominio más grande dentro de las variables n), esto es porque Xi tiene a lo sumo d elementos a suprimir de su dominio.  LA comprobación de consistencia de arco puede hacerse O(d^2), teniendo en cuenta la cantidad de arcos y la modificación que se incorporó para evitar la verificación de arcos ya consistentes, la complejidad de la arco consistencia quedaría como O(n^2 d^2)
#### 5. Demostrar la correctitud del algoritmo CSP para  árboles estructurados (sección 5.4, p. 172 AIMA 2da edición). Para ello, demostrar:
#####   a. Que para un CSP cuyo grafo de restricciones es un árbol, 2-consistencia (consistencia de arco) implica n-consistencia (siendo n número total de variables)
#####   b. Argumentar por qué lo demostrado en a es suficiente. 

a)

Hay 3 pasos en la resolución:

Generar el árbol estructurado de manera tal que el grafo de restricciones se componga únicamente de nodos padre-hijo, dejándonos con el único problema de resolver arco-consistencia en lugar de n-consistencia.

Lograr el arco consistencia en el sentido contrario, eliminando los valores de los respectivos dominios.

Asignar valores válidos del dominio a cada una de las variables.

La idea detrás de estos pasos es la de convertir un problema en la que debemos resolver no-consistencia, en uno en el que solo debemos resolver arco-consistencias. Gracias al paso 1, en el que convertimos un grafo en un árbol cuyas únicas "relaciones" que encontramos son padre e hijo, jamás nos hallaremos en la situación de tener que resolver una consistencia mayor que la arco-consistencia, es decir, solo nos encontraremos con restricciones binarias por la propia naturaleza del árbol. 
Por esto, si bien nuestro problema inicial contenía restricciones de más de dos variables, luego de esta conversión, sólo necesitamos obtener el arco-consistencia de las variables que se encuentran en el árbol, de esta forma, terminamos resolviendo las n variables.


b) Gracias al ejercicio anterior, llegamos a la conclusión de que es posible resolver un CSP cuyo grafo de restricciones es un árbol, mediante la arco-consistencia de cada una de sus variables, es decir, el algoritmo citado en el ejercicio anterior resulta correcto para todos los CSP cuyo grafo de restricciones pueda ser convertido en un árbol, a pesar de que en un principio parezca que tenemos que lidiar con la n-consistencia.
