import matplotlib.pyplot as plt # Por convención, se importa así para escribir menos
import numpy as np

# 1. La función limpia, sin globales y devolviendo el tiempo
def generador(frec, amp, dur, fs):
    t = np.arange(0, dur, 1/fs)
    signal = amp * np.sin(2 * np.pi * frec * t)
    return t, signal

# 2. Parámetros lógicos: 220 Hz de frecuencia, Amplitud 1, duración cortita
if __name__ == "__main__":
    try:
        # Parámetros
        frec = 220
        amp = 1
        dur = 0.02
        fs_cont = 44100   # resolución continua
        fs_samp = 2000    # frecuencia de muestreo para discretizar (ajusta si quieres)

        # Generar señal continua
        t, signal = generador(frec=frec, amp=amp, dur=dur, fs=fs_cont)

        # Generar instantes de muestreo y obtener muestras via interpolación
        t_s = np.arange(0, dur, 1/fs_samp)
        signal_s = np.interp(t_s, t, signal)

        # Depuración mínima
        print(f"fs_cont={fs_cont}, fs_samp={fs_samp}, len(t)={t.size}, len(t_s)={t_s.size}")

        # Graficado
        plt.figure(figsize=(8, 4))
        plt.plot(t, signal, label=f'Continuo ({fs_cont} Hz)', linewidth=1)
        plt.stem(t_s, signal_s, linefmt='C1-', markerfmt='C1o', basefmt='k', label=f'Muestreo {fs_samp} Hz')
        plt.scatter(t_s, signal_s, color='C1')  # refuerzo visual de puntos muestreados

        plt.title('Señal Senoidal de 220 Hz y su versión discretizada')
        plt.xlabel('Tiempo (segundos)')
        plt.ylabel('Amplitud')
        plt.legend()
        plt.grid(True)
        plt.tight_layout()
        plt.show()

    except Exception as e:
        print("Error al ejecutar el script:", e)