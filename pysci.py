import numpy as np
import matplotlib.pyplot as plt # type: ignore
import sympy as sp # type: ignore

# Define the function to plot
def f(x):
    return np.sin(x) * np.exp(-0.1 * x)

# Define the symbolic variable and function for symbolic computation
x = sp.symbols('x')
f_sym = sp.sin(x) * sp.exp(-0.1 * x)

# Compute the derivative and integral symbolically
f_prime_sym = sp.diff(f_sym, x)
f_integral_sym = sp.integrate(f_sym, x)

# Convert symbolic expressions to numerical functions
f_prime = sp.lambdify(x, f_prime_sym, 'numpy')
f_integral = sp.lambdify(x, f_integral_sym, 'numpy')

# Generate x values
x_vals = np.linspace(0, 10, 400)

# Compute y values for the function, its derivative, and integral
y_vals = f(x_vals)
y_prime_vals = f_prime(x_vals)
y_integral_vals = f_integral(x_vals)

# Plot the function
plt.figure(figsize=(10, 6))
plt.subplot(3, 1, 1)
plt.plot(x_vals, y_vals, label='$f(x) = \sin(x) e^{-0.1x}$')
plt.title('Function')
plt.legend()
plt.grid(True)

# Plot the derivative
plt.subplot(3, 1, 2)
plt.plot(x_vals, y_prime_vals, label="$f'(x)$")
plt.title('Derivative')
plt.legend()
plt.grid(True)

# Plot the integral
plt.subplot(3, 1, 3)
plt.plot(x_vals, y_integral_vals, label='$\\int f(x) dx$')
plt.title('Integral')
plt.legend()
plt.grid(True)

# Adjust layout
plt.tight_layout()

# Show the plots
plt.show()
