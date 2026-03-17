import numpy as np
import matplotlib.pyplot as plt

# 1. Definir el vector de tiempo (1 segundo, 1000 muestras)
# Usamos endpoint=False para que el intervalo de 1 segundo sea exacto y 
# la ortogonalidad matemática se cumpla a la perfección.
t = np.linspace(0, 1, 1000, endpoint=False)

# 2. Generar la señal fija de 5 Hz
f_fija = 5.8
y_fija = np.sin(2 * np.pi * f_fija * t)

# 3. Lista de frecuencias a comparar
frecuencias = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
parecidos_k = [] # Lista para guardar los resultados del producto punto

# 4. Calcular el producto punto para cada frecuencia
for f in frecuencias:
    # Generar la señal variable con la frecuencia actual
    y_var = np.sin(2 * np.pi * f * t)
    
    # Calcular el producto punto (grado de parecido 'k')
    # np.dot suma la multiplicación punto a punto de ambos vectores
    k = np.dot(y_fija, y_var) 
    
    # Guardar el resultado
    parecidos_k.append(k)
    print(f"Frecuencia {f} Hz -> Grado de parecido (k): {k:.2f}")

# 5. Graficar los resultados en un gráfico de barras
plt.figure(figsize=(10, 6))
plt.bar(frecuencias, parecidos_k, color='skyblue', edgecolor='black')

# Configuraciones estéticas del gráfico
plt.title(f'Grado de parecido (Producto Punto) vs Señal fija de {f_fija} Hz', fontsize=14)
plt.xlabel('Frecuencia de la señal comparada (Hz)', fontsize=12)
plt.ylabel('Grado de parecido [k]', fontsize=12)
plt.xticks(frecuencias) # Para que muestre todos los números del 1 al 10 en el eje X
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Mostrar la gráfica
plt.show()