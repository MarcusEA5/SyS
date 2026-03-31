import numpy as np
import matplotlib.pyplot as plt

# 1. Definir los parámetros del ejercicio
f1 = 10        # Hz
f2 = 20        # Hz
Tm = 0.001     # segundos (período de muestreo)

# 2. Crear el vector de tiempo discreto
# Usamos np.arange para ir desde 0 hasta 1 (inclusive) dando saltos del tamaño de Tm
t = np.arange(0, 1 + Tm, Tm) 

# El índice 'n' es intrínseco a la posición en el arreglo 't'
# 3. Generar la señal discreta s[n]
s_n = np.sin(2 * np.pi * f1 * t) + 4 * np.sin(2 * np.pi * f2 * t)

# 4. Graficar los resultados
plt.figure(figsize=(12, 5))

# Como hay 1000 muestras, si graficamos todo de 0 a 1 segundo se va a ver muy apretado.
# Vamos a graficar solo las primeras 200 muestras (0.2 segundos) para ver bien la morfología.
plt.plot(t[:200], s_n[:200], color='teal', marker='.', markersize=4, linestyle='-', linewidth=1)

plt.title('Versión discreta de la señal s[n]')
plt.xlabel('Tiempo (s)')
plt.ylabel('Amplitud s[n]')
plt.grid(True, linestyle='--', alpha=0.7)

# Mostrar la gráfica
plt.tight_layout()
plt.show()
