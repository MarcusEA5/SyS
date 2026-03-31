import numpy as np
import matplotlib.pyplot as plt

# 1. Parámetros iniciales (igual que antes)
f1 = 10        # Hz
f2 = 10.5        # Hz
Tm = 0.001     # s (período de muestreo)
fs = 1 / Tm    # Frecuencia de muestreo (1000 Hz)

# 2. Vector de tiempo discreto (exactamente 1 segundo -> 1000 muestras)
t = np.arange(0, 1, Tm)
N = len(t) # N = 1000 muestras

# 3. Señal discreta s[n]
s_n = np.sin(2 * np.pi * f1 * t) + 4 * np.sin(2 * np.pi * f2 * t )

# --- CÁLCULO DE LA TDF ---

# 4. Calcular la FFT
S_k = np.fft.fft(s_n)

# 5. Calcular la magnitud y normalizar
# Normalizamos dividiendo por N/2 para recuperar las amplitudes originales (1 y 4)
magnitud_normalizada = np.abs(S_k) / (N / 2)

# 6. Crear el eje X de frecuencias
frecuencias = np.fft.fftfreq(N, d=Tm)

# --- PREPARACIÓN PARA GRAFICAR CON BARRAS ---

# Tomamos solo la mitad positiva del espectro
mitad = N // 2
frec_positivas = frecuencias[:mitad]
magnitud_positiva = magnitud_normalizada[:mitad]

# 7. Graficar usando plt.bar()
plt.figure(figsize=(10, 5))

# Definimos el ancho de la barra. Como la resolución frecuencial es 1Hz (1s de duración),
# un ancho de 0.7 o 0.8 deja un lindo espacio entre barras.
plt.bar(frec_positivas, magnitud_positiva, width=0.8, color='crimson', edgecolor='black', alpha=0.8)

# Recortamos la gráfica en el eje X para ver los picos de interés
plt.xlim(0, 50) 
plt.ylim(0, 4.5)

# Configuraciones estéticas
plt.title('Espectro de Magnitud de $s[n]$ (Gráfico de Barras)', fontsize=14)
plt.xlabel('Frecuencia (Hz)', fontsize=12)
plt.ylabel('Magnitud (Amplitud de la Senoide)', fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.5) # Grilla solo horizontal

plt.tight_layout()
plt.show()