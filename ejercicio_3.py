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
    print(f"El promedio del tiempo de ejecución por servidor de la columna {k+1} es {promedio}")


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

#Parte D.7:

tiempos_totales = []
for i in range(3):
    fila = []
    for k in range(3):
        producto = matriz_M[i][k] * matriz_c[i][k]
        fila.append(producto)
    tiempos_totales.append(fila)
print("La matriz propuesta es: ")
for i in range(3):
    print(tiempos_totales[i])


#Parte E.9:

diagonal_abajo = 0
producto_1 = 0

for o in range(len(matriz_M)):
    producto_1 = 1
    matriz_ampliada = [[120,150,100],[200,180,220],[90,110,95]]
    for m in range(len(matriz_M) - 1):
        matriz_ampliada.append(matriz_M[m])
    for k in range(len(matriz_M)):
        producto_1 = producto_1 * matriz_ampliada[o][k]
        matriz_ampliada.pop(0)
    diagonal_abajo = diagonal_abajo + producto_1


diagonal_arriba=0
producto_1=0
for o in range(len(matriz_M)):
    producto_1 = 1
    matriz_ampliada = [[120,150,100],[200,180,220],[90,110,95]]
    for m in range(len(matriz_M) - 1):
        matriz_ampliada.append(matriz_M[m])
    for k in range(len(matriz_M)-1, -1,-1):
        producto_1 = producto_1 * matriz_ampliada[o][k]
        matriz_ampliada.pop(0)
    diagonal_arriba = diagonal_arriba + producto_1
    
det=diagonal_abajo-diagonal_arriba

print(f"El determinante de la matriz M es: {det}")

#Parte F.11
#Funcion de mayor costo computacional
matriz_promedio=[]
for i in range(3):
    suma=0
    for k in range(3):
        suma=suma+matriz_M[i][k]
    promedio=suma/3
    matriz_promedio.append(promedio)
print(matriz_promedio)
mayor=matriz_promedio[0]
fila_mayor=0
for i in range(1,3):
    if matriz_promedio[i]>mayor:
        mayor=matriz_promedio[i]
        fila_mayor=i       
print(f"La funcion de mayor costo es la funcion {fila_mayor+1} y vale {mayor} ")

#Servidor mas eficiente
matriz_promedio=[]
for k in range(3):
    suma=0 
    for i in range(3):
        suma=suma+matriz_M[i][k]
    promedio=suma/3
    matriz_promedio.append(promedio)
menor=matriz_promedio[0]
columna_menor=0
for k in range(1,3):
    if matriz_promedio[k]<menor:
        menor=matriz_promedio[k]
        columna_menor=k
print(f"El servidor mas eficiente es el servidor {columna_menor+1} y vale {menor}")


