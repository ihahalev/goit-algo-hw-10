import numpy as np
import scipy.integrate as spi

def monte_carlo_integrate(f, a, b, N):
    x = np.random.uniform(a, b, N)
    y = np.random.uniform(0, f(b), N)
    inside = y < f(x)
    integral = (b - a) * f(b) * np.sum(inside) / N
    return integral, x, y, inside

def analytic_integrate(f, a, b):
    integral, _ = spi.quad(f, a, b)
    return integral
