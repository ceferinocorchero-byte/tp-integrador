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
union_ab=[]

for i in lista_a:
    repetido=False
    for x in union_ab:
        if x==i:
            repetido=True
    if repetido==False:
        union_ab.append(i)

for k in lista_b:
    repetido=False
    for x in union_ab:
        if x==k:
            repetido=True
    if repetido==False:
        union_ab.append(k)

print("Los usuarios que utilizan al menos una plataforma son: \n" + str(union_ab))

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

# parte A.1: Usuarios que utilizan exclusivamente una sola plataforma
usuarios_una_plataforma = []
for i in lista_a:
    if i not in lista_b:
        if i not in usuarios_una_plataforma:
            usuarios_una_plataforma.append(i)

for i in lista_b:
    if i not in lista_a:
        if i not in usuarios_una_plataforma:
            usuarios_una_plataforma.append(i)

print("Los usuarios que usan una sola plataforma son:\n" + str(usuarios_una_plataforma))


# parte A.3: Usuarios que aparecen en C perno no en A U B

usuarios_especiales = []

for i in lista_c:
    if i not in (lista_a or lista_b):
        usuarios_especiales.append(i)
print("Los usuarios que aparecen en C pero no en A U B son: \n" + str(usuarios_especiales))

# parte B.6: usuarios que utilizan la API o la web y que presentan errores

usuarios_con_errores = []
for i in union_ab: #union_ab es la lista con usuarios que utilizan al menos una plataforma, definida en el punto A.1
    if i in lista_c:
        usuarios_con_errores.append(i)
print("Los usuarios que sí presentan errores son: \n" + str(usuarios_con_errores))

# parte B.7: usuarios criticos y no criticos
# Nota: union_ab es la lista de usuarios que pertenecen a lista_a o lista_b
usuarios_criticos = []
usuarios_no_criticos = []

for i in union_ab:
    if i in lista_c:
        usuarios_criticos.append(i)
for i in union_ab:
    if i not in usuarios_criticos:
        usuarios_no_criticos.append(i)

print("Usuarios criticos:")
print(usuarios_criticos)

print("Usuarios no criticos:")
print(usuarios_no_criticos)
