import numpy as np
import matplotlib.pyplot as plt
import random

# Definimos la función a optimizar (ejemplo: una función con múltiples máximos y mínimos)
def function(x):
    return np.sin(10 * np.pi * x) / x

# Parámetros del algoritmo genético
POPULATION_SIZE = 20
GENERATIONS = 50
MUTATION_RATE = 0.1

# Inicialización de la población (valores aleatorios en un rango determinado)
population = np.random.uniform(0.1, 2, POPULATION_SIZE)

# Visualización inicial
x = np.linspace(0.1, 2, 1000)
y = function(x)
plt.plot(x, y, label="Función a optimizar")
plt.scatter(population, function(population), color='red', label="Población inicial")
plt.legend()
plt.title("Optimización con Algoritmos Genéticos")
plt.show()
