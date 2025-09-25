import numpy as np
import matplotlib.pyplot as plt

#simulate simple 1D shock-turbulent interaction
x = np.linspace(0, 1, 100)
u = np.sin(2 * np.pi * x)  #turbulent velocity
shock = np.heaviside(x-0.5, 1)  #shock at center
interaction = u + shock

plt.plot(x, interaction)
plt.title("Shock-Turbulent Boundary Layer Interaction")
plt.xlabel("x")
plt.ylabel("velocity")
plt.grid(True)
plt.show()
