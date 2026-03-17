import numpy as np
import matplotlib.pyplot as plt
import random

def generar_senoide(frec, fase, t):
    # Generamos una amplitud random entre 1.0 y 5.0
    amp_random = random.uniform(1.0, 5.0)
    
    # Armamos la ecuación paramétrica de la señal
    senal = amp_random * np.sin(2 * np.pi * frec * t + fase)
    
    return senal, amp_random

# 1. Definimos el vector de tiempo
t = np.linspace(0, 1, 1000)

print("--- GENERADOR DE SEÑALES ---")

# 2. Pedimos los datos de la PRIMERA señal
print("\nConfigurando la Señal 1:")
frec1 = float(input("Ingresá la frecuencia en Hz (ej: 3): "))
fase1 = float(input("Ingresá la fase en radianes (ej: 0): "))
x1, amp1 = generar_senoide(frec1, fase1, t)
print(f"-> Máquina asignó una amplitud aleatoria de: {amp1:.2f}")

# 3. Pedimos los datos de la SEGUNDA señal
print("\nConfigurando la Señal 2:")
frec2 = float(input("Ingresá la frecuencia en Hz (ej: 7): "))
fase2 = float(input("Ingresá la fase en radianes (ej: 1.57): "))
x2, amp2 = generar_senoide(frec2, fase2, t)
print(f"-> Máquina asignó una amplitud aleatoria de: {amp2:.2f}")

# 4. Sumamos ambas señales (Principio de Superposición)
y_suma = x1 + x2

# 5. Graficamos el resultado con las 3 ondas
plt.figure(figsize=(12, 6))

# Graficamos las ondas originales (de fondo, punteadas y con algo de transparencia)
plt.plot(t, x1, color='blue', linestyle='--', alpha=0.6, label=f'Señal 1 ({frec1} Hz)')
plt.plot(t, x2, color='green', linestyle='--', alpha=0.6, label=f'Señal 2 ({frec2} Hz)')

# Graficamos la suma (bien gruesa y solida en primer plano)
plt.plot(t, y_suma, color='purple', linewidth=2.5, label='Señal Resultante (Suma)')

# Detalles estéticos del gráfico
plt.title('Superposición de Señales Paramétricas Senoidales')
plt.xlabel('Tiempo $t$ (segundos)')
plt.ylabel('Amplitud $y(t)$')
plt.axhline(0, color='black', linewidth=1) # Línea del eje X
plt.legend(loc='upper right')
plt.grid(True, linestyle='--', alpha=0.7)

plt.tight_layout()
plt.show()