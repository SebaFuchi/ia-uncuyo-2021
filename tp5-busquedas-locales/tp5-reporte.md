# GRAFICOS #
## A .5 (Distribucion de tiempo)

#### Hill Climbing
##### 4 reinas

![image](https://user-images.githubusercontent.com/61237150/133837082-cc4e82b7-f517-4794-a3ca-e59c23fbb90b.png)

##### 8 reinas

![image](https://user-images.githubusercontent.com/61237150/133837119-f6ce2c81-ca23-4d18-926c-263fc1c98cc1.png)

##### 10 reinas

![image](https://user-images.githubusercontent.com/61237150/133837179-9d6f2c5c-63d3-4b9f-9621-2b2cc3063693.png)

#### Simulated Annealing
##### 4 reinas

![image](https://user-images.githubusercontent.com/61237150/133837215-08a3d2e1-a7bf-4676-9c3c-475cd0a185fd.png)

##### 8 reinas

![image](https://user-images.githubusercontent.com/61237150/133837238-1c94976c-9d67-4c20-b746-c5f22fb392c6.png)

##### 10 reinas

![image](https://user-images.githubusercontent.com/61237150/133837268-0f1b5ffd-4687-4747-a4ea-c970a8eeb4ce.png)

#### Genetic
##### 4 reinas

![image](https://user-images.githubusercontent.com/61237150/133837309-9586c700-66a6-4fad-95c8-bab205bedadf.png)

##### 8 reinas

![image](https://user-images.githubusercontent.com/61237150/133837343-bccbcbe9-52fa-4b37-bc5a-e1821184570d.png)

##### 10 reinas

![image](https://user-images.githubusercontent.com/61237150/133837379-6083fb65-3ba1-4015-baf0-aae75a0aca20.png)

## B (Variacion de la funcion h())
#### Hill Climbing

![image](https://user-images.githubusercontent.com/61237150/133837470-1225f063-ec05-45a3-bb06-e69bbee67665.png)

#### Simulated Annealing

![image](https://user-images.githubusercontent.com/61237150/133837503-33739a96-8369-45cf-baa5-935a1c33590d.png)

#### Genetic

##### Almacenando los valores de todos los hijos de cada generacion
![image](https://user-images.githubusercontent.com/61237150/133837537-7a1fddef-f005-4034-ae27-85b297732d36.png)

##### Almacenando el valor del mejor hijo de cada generacion
![image](https://user-images.githubusercontent.com/61237150/133837671-8f009259-a888-4e6b-b33f-200b75603006.png)

## C (Conclusion)

Mediante un análisis y comparación de los datos que se obtuvieron de cada uno de los diferentes algoritmos, llego a la conclusión que Simulated Annealing es el algoritmo mas óptimo para este problema. Esto se debe a que me permite escapar del problema que presenta Hill Climbing, los máximos o mínimos locales, con el uso de la probabilidad, puedo escapar de esto, mejorando enormemente los resultados.

A su vez, es mejor que un algoritmo genético, ya que a medida que el problema crece, se tienen que incorporar mas sujetos a la población y mas generaciones, esto retarda el proceso de encontrar una solución y me fuerza a recorrer muchos mas estados antes de dar con la solución óptima.

Simulated Annealing me brinda el resultado mas óptimo un mayor porcentaje de veces que Hill Climbing y a su vez es mas eficiente con el uso del tiempo y estados que un algoritmo genético.
