## 2.10 ##

### A. ###

No, ya que aunque se lo penalice, el agente no cuenta con algún mecanismo para aprender de los acciones pasadas, por lo que a esta implementación le es irrelevante si se la premia o se la penaliza

### B. ###

Si se tratara de un agente reflexivo con estados, una forma de afrontar el problema seria implementando una especie de mapeo de memoria, en la que el agente "recuerde" o sepa en que casillas ya estuvo para intentar evitarlas. Esta implementación seria enfocada a eficientizar los movimientos, priorizando los lugares por los que no paso para verificar su estado.

### C. ###

Si se diera el caso en el que el agente conociera todo su entorno, en el caso A, seria un agente mucho mas racional, ya que podría modificarse su implementación para que se dirija a los nodos sucios.

En el caso del agente con estados, este perdería un poco de sentido, ya que si el agente de ante mano conoce todo el entorno, sabe que cosas están sucias y cuales no, por lo que no le seria necesario "recordar" por donde ya paso, simplemente se actualizaría su conocimiento sobre el terreno general.

Para ambos casos, se debería implementar un sistema, por ejemplo, basado en grafos, que le permita optimizar y crear rutas que requieran menos movimientos para limpiar lo mas posible.

## 2.11 ##

### A. ###

Este caso es igual al anterior, el agente posee tan poco conocimiento del entorno, que no se puede prever ni anticipar movimientos, solo conoce su posición actual, sin capacidad de recordar movimientos pasados, por lo que  sea cual sea la disposición del terreno, este agente seguirá siendo igual de irracional.

### B. ###

Estadísticamente, haciendo pruebas, llegue a la conclusión de que un agente aleatorio es mas ineficiente que un agente reflexivo, ya que todas sus acciones son al azar, no solo su movimiento, puede decidir no limpiar un lugar sucio, no moverse o limpiar lugares limpios, por ejemplo. De esta, manera se desperdician movimientos.
Mientras mas pequeño es el entorno, por la cantidad de movimientos, es probable que ambos agentes logren resultados muy similares, pero a medida que se agranda el tablero, el rendimiento del agente aleatorio decae abruptamente.

### C. ###

Como se dijo anteriormente, un agente aleatorio que trabaja sobre un espacio muy amplio, tiende a ser mucho mas ineficiente que un agente reflexivo simple, dado que al ser aleatorio, las posibilidades de realizar combinaciones exitosas entre movimiento y limpieza, decaen.

### D. ###

Un agente con estados superara ampliamente a un agente reflexivo simple ya que recordara sus movimientos previos, de esta forma, se intentaría optimizar el rendimiento del agente, aprovechándose de esta "memoria" si se le quiere decir, haciendo que el agente con estado evite los lugares que ya limpio o los obstáculos del terreno, Un agente simple tiene mas probabilidades de volver a un lugar en el que ya estuvo o toparse con un obstáculo repetidas veces.