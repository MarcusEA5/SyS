import numpy as np

# 1. Parámetros iniciales
f1 = 10        # Hz
f2 = 20        # Hz
Tm = 0.001     # s (período de muestreo)

# 2. Vector de tiempo discreto (1000 muestras)
t = np.arange(0, 1, Tm)
N = len(t)

# 3. Generar la señal discreta s[n]
s_n = np.sin(2 * np.pi * f1 * t) + 4 * np.sin(2 * np.pi * f2 * t)

# --- VERIFICACIÓN DEL TEOREMA DE PARSEVAL ---

# 4. Calcular la energía total en el dominio del TIEMPO
# Fórmula: Suma de ( |s[n]|^2 )
energia_tiempo = np.sum(np.abs(s_n)**2)

# 5. Calcular la TDF (S[k]) usando FFT
S_k = np.fft.fft(s_n)

# 6. Calcular la energía total en el dominio de la FRECUENCIA
# Fórmula: (1 / N) * Suma de ( |S[k]|^2 )
energia_frecuencia = (1 / N) * np.sum(np.abs(S_k)**2)

# 7. Mostrar resultados
print(f"Energía calculada en el tiempo:     {energia_tiempo:.4f}")
print(f"Energía calculada en la frecuencia: {energia_frecuencia:.4f}")

# Utilizamos np.isclose() porque los decimales flotantes pueden tener errores minúsculos
son_iguales = np.isclose(energia_tiempo, energia_frecuencia)
print(f"¿Se cumple la relación de Parseval? {son_iguales}")