#Parte A.3: Calculo de intersección

m1 = 40 #Pendiente de la ecuacion a
b1 = 200 #Ordenada al origen de la ecuacion a

m2 = 70 #Pendiente de la ecuacion b
b2 = 50 #Ordenada al origen de la ecuacion b

x = (b1 - b2) / (m2 - m1) #Calculo de la coordenada x del punto de intersección

y = m1 * x + b1 #Reemplazamos la coordenada x para encontrar la coordenada
print("Punto de interseccion:")
print("x =", x)
print("y =", y)

#Parte A.4: Calculo del vertice de la ecuación C

b=80
a=-2
c=100
vertice_x=-b/(2*a) #Calculo del vertice x

#Evaluamos la expresión en la coordenada x obtenida:
vertice_y= -2*(vertice_x**2) +80*vertice_x +100 

print(f"La coordenada del vertice es: ({vertice_x};{vertice_y})")


#Calculo de las raices

raiz_1=(-b+((b**2)-(4*a*c))**(1/2))/(2*a)
raiz_2=(-b-((b**2)-(4*a*c))**(1/2))/(2*a)

print("Las raices son:")
print(f"Raiz 1= {raiz_1}")
print(f"Raiz 2= {raiz_2}")



#Parte B.5
#Ecuaciones del enunciado 5:

x=int(input())

a = 40 *x + 200
b = 70 *x + 50
c = -2 * (x ** 2) + 80 * x + 100

#Parte B.7
#Evaluar las funciones para los valores:

valores = [0, 5, 10, 15, 20, 25, 30, 40, 50]

for x in valores:
    
    a = 40 *x + 200
    b = 70 *x + 50
    c = -2 * (x ** 2) + 80 * x + 100
    

    
    print("Para x =", x)
    print("A(x) =", a)
    print("B(x) =", b)
    print("C(x) =", c)


#Punto B.8
#Crear una funcion que determine el plan mas economico para un valor de x


valores = [0, 5, 10, 15, 20, 25, 30, 40, 50]

for x in valores:
    
    a = 40 *x + 200
    b = 70 *x + 50
    c = -2 * (x ** 2) + 80 * x + 100
    print(f"Para x={x}", end=" ")
    if a < b and a < c:
        print(f"El plan mas economico es A con un valor de: {a}")

    elif b < a and b < c:
        print(f"El plan mas economico es B con un valor de: {b}")

    else:
        print(f"El plan mas economico es C con un valor de: {c}")

    
    


