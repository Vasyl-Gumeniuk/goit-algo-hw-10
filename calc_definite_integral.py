import numpy as np
import scipy.integrate as spi
import matplotlib.pyplot as plt


# ЗАВДАННЯ 1
# Визначення функції
def f(x):
    return x ** 2

# Визначення меж інтегрування
a = 0  # Нижня межа
b = 2  # Верхня межа

# Генерація випадкових точок
n = 100000  # Кількість випадкових точок
x_random = np.random.uniform(a, b, n)
y_random = np.random.uniform(0, f(b), n)

# Обчислення кількості точок, які потрапляють під криву
points_under_curve = sum(y_random < f(x_random))

# Обчислення відношення площі під кривою до загальної площі
integral_value = (points_under_curve / n) * (b - a) * f(b)

# Виведення інтеграла методом Монте-Карло
print("Значення інтеграла методом Монте-Карло:", integral_value)


# ЗАВДАННЯ 2
# Обчислення інтеграла за допомогою функції quad
result_quad, _ = spi.quad(f, a, b)

# Виведення інтеграла обчисленого за допомогою функції quad
print("Інтеграл, обчислений за допомогою quad:", result_quad)




# Побудова графіка функції та області під кривою
x = np.linspace(a, b, 400)
y = f(x)

fig, ax = plt.subplots()

ax.plot(x, y, 'r', linewidth=2)
ax.fill_between(x_random, y_random, color='gray', alpha=0.3)
ax.set_xlim([a, b])
ax.set_ylim([0, max(y_random)])
ax.set_xlabel('x')
ax.set_ylabel('f(x)')
ax.axhline(0, color='black', linewidth=0.5)
ax.axvline(0, color='black', linewidth=0.5)
ax.grid(True, linestyle='--', linewidth=0.5)
ax.set_title('Графік інтегрування f(x) = x^2 від ' + str(a) + ' до ' + str(b))

plt.show()
