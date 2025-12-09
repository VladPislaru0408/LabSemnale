import numpy as np
import matplotlib.pyplot as plt

# ex4 - sinusoida + sawtooth
fs = 1000
t = np.linspace(0, 1, fs)

# sinusoida
sin_signal = np.sin(2*np.pi*5*t)

# sawtooth 
f_saw = 5
saw_signal = 2 * np.mod(f_saw * t, 1) - 1

# suma
suma = sin_signal + saw_signal

fig, ax = plt.subplots(3)
ax[0].plot(t, sin_signal)
ax[0].set_title('Sinusoida')
ax[1].plot(t, saw_signal)
ax[1].set_title('Sawtooth')
ax[2].plot(t, suma)
ax[2].set_title('Suma')
plt.tight_layout()
plt.savefig('Lab2/ex4.pdf')
plt.show()
