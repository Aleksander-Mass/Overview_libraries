### 3. Библиотека `matplotlib`

# `matplotlib` используется для создания графиков и визуализации данных. Она позволяет строить линейные графики, гистограммы,
# диаграммы и многие другие виды визуализаций.

###    Пример использования `matplotlib`:
    
import matplotlib.pyplot as plt
import numpy as np

# 1. Создание линейного графика
x = np.linspace(0, 10, 100)
y = np.sin(x)
plt.plot(x, y, label="Sine Wave")
plt.title("Sine Function")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.legend()
plt.show()

# 2. Построение гистограммы
data = np.random.normal(0, 1, 1000)
plt.hist(data, bins=30, color='blue', alpha=0.7)
plt.title("Histogram")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.show()

# 3. Построение scatter plot
x = np.random.rand(50)
y = np.random.rand(50)
colors = np.random.rand(50)
sizes = 1000 * np.random.rand(50)

plt.scatter(x, y, c=colors, s=sizes, alpha=0.5)
plt.title("Scatter Plot")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.show()