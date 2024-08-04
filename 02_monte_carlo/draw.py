import matplotlib.pyplot as plt
import numpy as np

# Створення діапазону значень для x
def draw_integral(f, a, b, x_random, y_random, inside):
    x = np.linspace(-0.5, 2.5, 400)
    y = f(x)

    _, ax = plt.subplots()

    # Малювання функції
    ax.plot(x, y, 'g', linewidth=2)

    # Заповнення області під кривою
    ix = np.linspace(a, b)
    iy = f(ix)
    ax.fill_between(ix, iy, color='gray', alpha=0.3)

    # Відображення випадкових точок
    ax.scatter(x_random, y_random, color='black', s=1, label='Точки поза кривою')
    ax.scatter(x_random[inside], y_random[inside], color='red', s=1, label='Точки в середині кривої')

    # Налаштування графіка
    ax.set_xlim([x[0], x[-1]])
    ax.set_ylim([0, max(y) + 0.1])
    ax.set_xlabel('x')
    ax.set_ylabel('f(x)')

    # Додавання меж інтегрування та назви графіка
    ax.axvline(x=a, color='gray', linestyle='--')
    ax.axvline(x=b, color='gray', linestyle='--')
    ax.set_title(f'Графік f(x) = x^2 від {a} до {b}')
    plt.legend()
    plt.grid()
    plt.show()