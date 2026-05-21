#Parte B.3
#Implementacion en python

matriz_M= [ [120,150,100]
           ,[200,180,220]
           ,[90, 110 ,95]]

#El tiempo promedio de ejecución por función
for i in range(3):
    suma=0
    for k in range(3):
        suma=suma+matriz_M[i][k]
    promedio=suma/3
    print(f"El promedio del tiempo de ejecucion por funcion de la fila {i+1} es {promedio}")

#El tiempo promedio de ejecución por servidor
for k in range(3):
    suma=0 
    for i in range(3):
        suma=suma+matriz_M[i][k]
    promedio=suma/3
    print(f"El promedio del tiempo de ejecución por función de la columna {k+1} es {promedio}")


#Parte B.4
#Calcular la matriz transpuesta de M y explicar qué representa en este contexto

matriz_T=[[],[],[]]

for i in range(3):
    for k in range(3):
        matriz_T[i].append(matriz_M[k][i])
    print(matriz_T[i])



#Parte C.5
#Calcular el producto 𝑇=𝑀∗𝐶

matriz_c=[[30,20,10],
          [15,25,20],
          [40,10,30]]




T= []

for i in range(3):

    fila = []

    for j in range(3):

        suma = 0

        for k in range(3):

            suma = suma + matriz_M[i][k] * matriz_c[k][j]

        fila.append(suma)

    T.append(fila)

for i in range(3):
    print(T[i])