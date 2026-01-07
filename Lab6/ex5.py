import numpy as np
import matplotlib.pyplot as plt

def dreptunghiulara(N):
    fereastra = np.zeros(N)
    return fereastra

def hanning(N):
    n = np.arange(N)
    return 0.5 - 0.5 * np.cos(2 * np.pi * n / (N - 1))

f = 100
A = 1
phi = 0
Nw = 200
fs = 10000

t = np.arange(Nw) / fs
sinusoida = A * np.sin(2 * np.pi * f * t + phi)

fereastra_drept = dreptunghiulara(Nw)
fereastra_hann = hanning(Nw)

semnal_drept = sinusoida * fereastra_drept
semnal_hann = sinusoida * fereastra_hann

fig, axes = plt.subplots(3, 2, figsize=(12, 10))

axes[0, 0].plot(fereastra_drept)
axes[0, 0].set_title('Fereastra dreptunghiulara')
axes[0, 0].grid(True)

axes[0, 1].plot(fereastra_hann)
axes[0, 1].set_title('Fereastra Hanning')
axes[0, 1].grid(True)

axes[1, 0].plot(sinusoida)
axes[1, 0].set_title('Sinusoida originala')
axes[1, 0].grid(True)

axes[1, 1].plot(sinusoida)
axes[1, 1].set_title('Sinusoida originala')
axes[1, 1].grid(True)

axes[2, 0].plot(semnal_drept)
axes[2, 0].set_title('Sinusoida cu fereastra dreptunghiulara')
axes[2, 0].grid(True)

axes[2, 1].plot(semnal_hann)
axes[2, 1].set_title('Sinusoida cu fereastra Hanning')
axes[2, 1].grid(True)

plt.tight_layout()
plt.savefig('ex5.pdf')
plt.show()
