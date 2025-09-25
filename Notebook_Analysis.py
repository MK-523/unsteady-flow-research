basic analysis of unsteady flow data.

```python
import numpy as np
import matplotlib.pyplot as plt

#example turbulence signal
t = np.linspace(0, 1, 500)
signal = np.sin(20*np.pi*t) + 0.5*np.random.randn(len(t))

plt.plot(t, signal)
plt.title("Example Turbulent Signal")
plt.xlabel("time (s)")
plt.ylabel("velocity fluctuation")
plt.grid(True)
plt.show()

#compute FFT to analyze frequency content
fft_signal = np.fft.fft(signal)
freqs = np.fft.fftfreq(len(t), t[1]-t[0])

plt.plot(freqs[:len(freqs)//2], np.abs(fft_signal[:len(freqs)//2]))
plt.title("Frequency Spectrum of Turbulent Signal")
plt.xlabel("frequency (Hz)")
plt.ylabel("amplitude")
plt.grid(True)
plt.show()
