#Generar una señal utilizando la funcion seno cardinal y graficarla

import matplotlib.pyplot as plt
import numpy as np
def sinc(x):
    return np.sinc(x/np.pi) 
def generador_sinc(frec, amp, dur, fs):
    t = np.arange(-dur/2, dur/2, 1/fs)
    signal = amp * sinc(2 * np.pi * frec * t)
    return t, signal
  
try:
    frec = 220
    amp = 1
    dur = 0.02
    fs = 44100
    t, signal = generador_sinc(frec, amp, dur, fs)
    plt.figure(figsize=(14, 4))
    plt.plot(t, signal)
    plt.title('Señal Sinc')
    plt.xlabel('Tiempo (segundos)')
    plt.ylabel('Amplitud')
    plt.grid(True)
    plt.show()
except Exception as e:
    print("Error al ejecutar el script:", e)



