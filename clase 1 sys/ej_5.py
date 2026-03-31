import numpy as np
<<<<<<< HEAD
import matplotlib.pyplot as plt
=======

# Parámetros de la distribución gaussiana
mu = 0  # Media
sigma = 1  # Desviación estándar
N = 1000  # Largo de cada realización
M = 100  # Número de realizaciones

# Generar señales aleatorias gaussianas
signals = np.random.normal(mu, sigma, (M, N))

# Calcular media temporal para cada realización
temporal_means = np.mean(signals, axis=1)

# Calcular media de conjunto
ensemble_mean = np.mean(temporal_means)

# Calcular varianza temporal para cada realización
temporal_vars = np.var(signals, axis=1)

# Calcular varianza de conjunto
ensemble_var = np.mean(temporal_vars)

# Imprimir resultados
print(f"Media de conjunto: {ensemble_mean}")
print(f"Media teórica: {mu}")
print(f"Varianza de conjunto: {ensemble_var}")
print(f"Varianza teórica: {sigma**2}")

# Verificación de ergodicidad: si la media y varianza de conjunto son cercanas a las teóricas,
# la señal es ergódica en media y varianza.
>>>>>>> 9c7a8d518e9d04af867eabb5abf38cd3e6313b52

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
