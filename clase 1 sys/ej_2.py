#Generar una señal aleatoria entre +1 y -1 y graficarla

import matplotlib.pyplot as plt
import random

def generador_aleatorio(dur, fs):
    t = [i/fs for i in range(int(dur*fs))]
    signal = [random.uniform(-1, 1) for _ in t]
    return t, signal

if __name__ == "__main__":
    try:
        dur = 0.02
        fs = 44100
        t, signal = generador_aleatorio(dur, fs)
        plt.figure(figsize=(14, 4))
        plt.plot(t, signal)
        plt.title('Señal Aleatoria')
        plt.xlabel('Tiempo (segundos)')
        plt.ylabel('Amplitud')
        plt.grid(True)
        plt.show()
    except Exception as e:
        print("Error al ejecutar el script:", e)

