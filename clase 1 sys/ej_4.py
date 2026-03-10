import numpy as np
import matplotlib.pyplot as plt

# Parámetros dados por el problema
f0 = 4000  # Frecuencia original (4000 Hz)
fs = 129   # Frecuencia de muestreo (129 Hz)
duracion = 2 # Segundos (para poder ver bien la onda resultante)

# 1. Discretización de la señal
t_n = np.arange(0, duracion, 1/fs)
x_n = np.sin(2 * np.pi * f0 * t_n)

# 2. Señal aparente (la que vamos a calcular abajo) para comparar visualmente
f_alias = 1 # Frecuencia estimada (1 Hz)
t_continua = np.linspace(0, duracion, 1000)
x_alias = np.sin(2 * np.pi * f_alias * t_continua)

# 3. Graficamos
plt.figure(figsize=(10, 5))

# Dibujamos cómo se vería la onda lenta de 1 Hz de fondo
plt.plot(t_continua, x_alias, color='blue', alpha=0.3, label='Señal aparente (1 Hz)')

# Dibujamos nuestras muestras discretizadas
plt.stem(t_n, x_n, linefmt='red', markerfmt='ro', basefmt='black', label='Muestras a 129 Hz')

plt.title('Efecto Aliasing: Señal de 4000 Hz muestreada a 129 Hz')
plt.xlabel('Tiempo (s)')
plt.ylabel('Amplitud')
plt.legend()
plt.grid(True, linestyle='--')
plt.show()