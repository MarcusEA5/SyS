#Discretiza una seña senoidal con frecuencia 5Hz, duracion de 1 segundo utilizando 
# una frecuencia de muestre de (1000, 100, 25, 10, 4, 1, 0.5 ) Hz, grafique y anailice los resultados.

import matplotlib.pyplot as plt
import numpy as np  
def generador(frec, amp, dur, fs):
    t = np.arange(0, dur, 1/fs)
    signal = amp * np.sin(2 * np.pi * frec * t)
    return t, signal    
try:
    frec = 5
    amp = 1
    dur = 1
    fs_list = [1000, 100, 25, 10, 4, 1, 0.5]
    plt.figure(figsize=(14, 8))
    for i, fs in enumerate(fs_list):
        t, signal = generador(frec=frec, amp=amp, dur=dur, fs=fs)
        plt.subplot(len(fs_list), 1, i+1)
        plt.plot(t, signal)
        plt.title(f'Señal Senoidal de {frec} Hz con muestreo de {fs} Hz')
        plt.xlabel('Tiempo (segundos)')
        plt.ylabel('Amplitud')
        plt.grid(True)
    plt.tight_layout()
    plt.show()
except Exception as e:
    print("Error al ejecutar el script:", e)