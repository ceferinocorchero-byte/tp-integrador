# Listas con los usuarios
lista_a = [101,102,103,104,105,106]
lista_b = [104,105,106,107,108]
lista_c = [102,105,109]

# parte A.1: usuarios que utilizan ambas plataformas
print("Los usuarios que usan ambas plataformas son:")
for i in range(6):
    for k in range(5):
        if lista_a[i] == lista_b[k]:
            print(lista_a[i])


# parte A.1: usuarios que utilizan al menos una plataforma
resultado=[]

for i in lista_a:
    repetido=False
    for x in resultado:
        if x==i:
            repetido=True
    if repetido==False:
        resultado.append(i)

for k in lista_b:
    repetido=False
    for x in resultado:
        if x==k:
            repetido=True
    if repetido==False:
        resultado.append(k)

print("Los usuarios que utilizan al menos una plataforma son: \n" + str(resultado))

# parte A.1: usuarion que utilizan la plataforma, pero que no presentan errores

usuarios_sin_errores = []
for i in lista_a:
    if i not in lista_c:
        if i not in usuarios_sin_errores:
            usuarios_sin_errores.append(i)

for i in lista_b:
    if i not in lista_c:
        if i not in usuarios_sin_errores:
            usuarios_sin_errores.append(i)
print("Los usuarios que no presentan errores son: \n" + str(usuarios_sin_errores))

