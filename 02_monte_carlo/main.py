from draw import draw_integral
from intagration import analytic_integrate, monte_carlo_integrate

# Визначення функції та межі інтегрування
def f(x):
    return x ** 2

a = 0  # Нижня межа
b = 2  # Верхня межа

def main():
    analitic = analytic_integrate(f,a,b)
    print(f"Аналітичний розв'язок: {analitic:.6f}")
    for N in [1000, 10000, 100000]:
        integral, x, y, inside = monte_carlo_integrate(f,a,b,N)
        print(f"Монте-Карло: {integral:.6f}, похибка: {abs(analitic-integral):.6f}")
        draw_integral(f,a,b,x,y,inside)

if __name__ == "__main__":
    main()