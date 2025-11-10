import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols, diff, lambdify

# Define variable
t = symbols('t')

# Define position function s(t)
s = 5*t**3 - 2*t + 7

# Derivative (velocity)
v = diff(s, t)

# Convert symbolic functions to numeric functions
s_func = lambdify(t, s)
v_func = lambdify(t, v)

# Generate time values
t_values = np.linspace(0, 5, 100)  

# Compute numerical values
s_values = s_func(t_values)
v_values = v_func(t_values)

plt.figure(figsize=(8,5))
plt.plot(t_values, s_values, label="Position s(t)")
plt.plot(t_values, v_values, label="Velocity v(t)")
plt.xlabel("Time (t)")
plt.ylabel("Value")
plt.title("Position and Velocity Over Time")
plt.legend()
plt.grid(True)
plt.show()


print("**********************************************")
