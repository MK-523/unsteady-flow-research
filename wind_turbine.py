import numpy as np
import matplotlib.pyplot as plt

#simulate simple 1D wind turbine blade noise
t = np.linspace(0, 0.02, 1000)  #time vector
blade_pass_freq = 50  #Hz, typical blade pass frequency
turbulence_noise = 0.2 * np.random.randn(len(t))
pressure_signal = np.sin(2 * np.pi * blade_pass_freq * t) + turbulence_noise

plt.plot(t, pressure_signal)
plt.title("Wind Turbine Aeroacoustics Simulation")
plt.xlabel("time (s)")
plt.ylabel("pressure fluctuation")
plt.grid(True)
plt.show()

#frequency analysis
fft_signal = np.fft.fft(pressure_signal)
freqs = np.fft.fftfreq(len(t), t[1]-t[0])

plt.plot(freqs[:len(freqs)//2], np.abs(fft_signal[:len(freqs)//2]))
plt.title("Frequency Spectrum of Wind Turbine Noise")
plt.xlabel("frequency (Hz)")
plt.ylabel("amplitude")
plt.grid(True)
plt.show()
