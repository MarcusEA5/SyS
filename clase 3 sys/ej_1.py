#Genere una señal s(t) = sin(2πf1t)+4sin(2πf2t),
#con f1 = 10 y f2 = 20 Hz, y obtenga su version discreta s[n] con perıodo de muestreo Tm = 0,001 seg.
#en el intervalo de tiempo t = [0 . . . 1] seg. 


import numpy as np
import matplotlib.pyplot as plt

# Parámetros
f1 = 10  # Hz
f2 = 20  # Hz
Tm = 0.001  # Período de muestreo en segundos
t_inicio = 0  # Tiempo inicial
t_fin = 1  # Tiempo final

# Generar vector de tiempo discreto
n = np.arange(t_inicio, t_fin + Tm, Tm)  # n desde 0 hasta 1000
t = n * Tm  # Tiempo correspondiente

# Generar la señal continua s(t)
s_t = np.sin(2 * np.pi * f1 * t) + 4 * np.sin(2 * np.pi * f2 * t)

# La versión discreta s[n] es s_t, ya que t = n * Tm
s_n = s_t

# Imprimir algunos valores para verificar
print("Primeros 10 valores de s[n]:")
print(s_n[:10])

# Graficar la señal
plt.figure(figsize=(10, 6))
plt.plot(t, s_n, label='s[n] = sin(2πf1t) + 4sin(2πf2t)')
plt.xlabel('Tiempo (s)')
plt.ylabel('Amplitud')
plt.title('Señal Discreta s[n]')
plt.legend()
plt.grid(True)
plt.show()