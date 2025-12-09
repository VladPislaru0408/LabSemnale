import numpy as np
import matplotlib.pyplot as plt

# ex1 - sin si cos 
A, f, phi = 1, 5, np.pi/4
t = np.linspace(0, 1, 1000)

x_sin = A * np.sin(4*np.pi*f*t + phi)
x_cos = A * np.cos(4*np.pi*f*t + phi - np.pi/2)

fig, ax = plt.subplots(2)
ax[0].plot(t, x_sin)
ax[0].set_title('Sinus')
ax[1].plot(t, x_cos)
ax[1].set_title('Cosinus echivalent')
plt.tight_layout()
plt.savefig('Lab2/ex1.pdf')
plt.show()
