import numpy as np
import matplotlib.pyplot as plt

#simulate simple jet noise (pressure fluctuations)
t = np.linspace(0, 0.01, 1000)
frequency = 5000  #Hz
pressure = np.sin(2 * np.pi * frequency * t) * np.exp(-500*t)  #damped sine

plt.plot(t, pressure)
plt.title("Supersonic Jet Noise Simulation")
plt.xlabel("time (s)")
plt.ylabel("pressure fluctuation")
plt.grid(True)
plt.show()
