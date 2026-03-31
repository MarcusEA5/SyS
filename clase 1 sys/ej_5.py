import numpy as np

# Parámetros de la distribución gaussiana
mu = 0  # Media
sigma = 1  # Desviación estándar
N = 1000  # Largo de cada realización
M = 100  # Número de realizaciones

# Generar señales aleatorias gaussianas
signals = np.random.normal(mu, sigma, (M, N))

# Calcular media temporal para cada realización
temporal_means = np.mean(signals, axis=1)

# Calcular media de conjunto
ensemble_mean = np.mean(temporal_means)

# Calcular varianza temporal para cada realización
temporal_vars = np.var(signals, axis=1)

# Calcular varianza de conjunto
ensemble_var = np.mean(temporal_vars)

# Imprimir resultados
print(f"Media de conjunto: {ensemble_mean}")
print(f"Media teórica: {mu}")
print(f"Varianza de conjunto: {ensemble_var}")
print(f"Varianza teórica: {sigma**2}")

# Verificación de ergodicidad: si la media y varianza de conjunto son cercanas a las teóricas,
# la señal es ergódica en media y varianza.

