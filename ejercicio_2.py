# 𝐴(𝑥) = 40𝑥 + 200
# 𝐵(𝑥) = 70𝑥 + 50
# 𝐶(𝑥) = −2𝑥**2 + 80𝑥 + 100
# Se trabajará en el siguiente dominio: 𝐷𝑓 = 0 ≤ 𝑥 ≤ 50

import matplotlib.pyplot as plt
import numpy as np

# ==========================================
# PUNTO 5: Programar las funciones en Python
# ==========================================

def A(x):
    return 40 * x + 200

def B(x):
    return 70 * x + 50

def C(x):
    return -2 * (x**2) + 80 * x + 100


# ==========================================
# PUNTO 7: Evaluar las funciones para los valores dados
# ==========================================

valores_x = [0, 5, 10, 15, 20, 25, 30, 40, 50]

print("--- EVALUACIÓN DE LOS PLANES DE COSTOS ---")
print(f"{'Horas (x)':<10} | {'Plan A(x)':<10} | {'Plan B(x)':<10} | {'Plan C(x)':<10}")
print("-" * 50)

for x_val in valores_x:
    costo_A = A(x_val)
    costo_B = B(x_val)
    costo_C = C(x_val)
    print(f"{x_val:<10} | {costo_A:<10} | {costo_B:<10} | {costo_C:<10}")

print("\n" + "="*50 + "\n")


# ==========================================
# PUNTO 6: Graficarlas en el intervalo dado (0 <= x <= 50)
# ==========================================

# Generamos 500 puntos entre 0 y 50 para que la curva de C se vea suave y perfecta
x_grafico = np.linspace(0, 50, 500)

# Configuramos el tamaño del gráfico
plt.figure(figsize=(10, 6))

# Dibujamos cada función con un color y estilo diferente
plt.plot(x_grafico, A(x_grafico), label="Plan A(x) = 40x + 200", color="blue", linewidth=2)
plt.plot(x_grafico, B(x_grafico), label="Plan B(x) = 70x + 50", color="green", linewidth=2)
plt.plot(x_grafico, C(x_grafico), label="Plan C(x) = -2x² + 80x + 100", color="red", linewidth=2, linestyle="--")

# Resaltamos con puntitos los valores específicos del Punto 7
plt.scatter(valores_x, [A(val) for val in valores_x], color="blue", zorder=5)
plt.scatter(valores_x, [B(val) for val in valores_x], color="green", zorder=5)
plt.scatter(valores_x, [C(val) for val in valores_x], color="red", zorder=5)

# Títulos, etiquetas de los ejes y personalización básica
plt.title("Análisis y Optimización de Costos de Desarrollo", fontsize=14, fontweight="bold")
plt.xlabel("Cantidad de Horas Mensuales (x)", fontsize=12)
plt.ylabel("Costo del Plan ($)", fontsize=12)
plt.xlim(0, 50)  # Forzamos el dominio indicado: 0 <= x <= 50
plt.ylim(0, 1000) # Ajustamos el límite vertical para que se aprecie el vértice de C en 900

# Añadimos la grilla de fondo y la leyenda para saber cuál es cuál
plt.grid(True, linestyle=":", alpha=0.6)
plt.legend(fontsize=11)

# Mostramos el gráfico en pantalla
plt.show()


#Esto fue generado por la IA desde el punto 5 al punto 7
