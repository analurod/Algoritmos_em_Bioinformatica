# Plotar um gráfico de dispersão (scatter) com 200 pontos aleatórios gerados com numpy.random.randn (eixos X e Y independentes).
# Gráfico deve ter titulo, rotulos nos eixos, cores dos pontos mapeadas pela distancia euclidiana ao centro
# use cmap='viridi), barra de cores (colobar) e grid.

import numpy as np
import matplotlib.pyplot as plt

x = np.random.randn(200)
y = np.random.randn(200)

dist = np.sqrt(x**2 + y**2)

plt.scatter(x, y, c=dist, cmap='viridis')
plt.title('Gráfico de dispersão com 200 pontos aleatórios')
plt.xlabel('Eixo X')
plt.ylabel('Eixo Y')
plt.colorbar(label='Distância euclidiana ao centro')
plt.grid(True)
plt.show()
