#Implementing Integrals using Python
import sympy as sp
from sympy.abc import x 
function = x**2
indefinite_integral = sp.integrate(function, x)

print(f"The indefinite integral of f(x) = x^2 is: {indefinite_integral}")
a, b = 1, 3
definite_integral = sp.integrate(function, (x, a, b))

print(f"The definite integral of f(x) = x^2 from {a} to {b} is: {definite_integral}")


import numpy as np
import matplotlib.pyplot as plt

#lambda x: x**2   fuction
#lambda x: x**3/3  integration function 
func_lambda = sp.lambdify(x, function, 'numpy')
integral_lambda = sp.lambdify(x, indefinite_integral, 'numpy')

# Generate x values
x_vals = np.linspace(0, 4, 100)
y_vals = func_lambda(x_vals)

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(x_vals, y_vals, label='f(x) = x^2', color='blue')
plt.fill_between(x_vals, y_vals, where=[(x_val >= a and x_val <= b) for x_val in x_vals], color='gray', alpha=0.5)
plt.title('Function and Area Under Curve')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.grid(True)
plt.show() 