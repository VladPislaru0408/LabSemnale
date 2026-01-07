import numpy as np
import matplotlib.pyplot as plt

# ex2 - infasurare pe cercul unitate
f = 7
N = 1000
n = np.linspace(0, 1, N)
x = np.sin(2*np.pi*f*n)

# Figura 1
y = x * np.exp(-2j*np.pi*n)

fig, ax = plt.subplots(1, 2, figsize=(10, 4))
ax[0].plot(n*N, x)
ax[0].set_title('Semnal')
ax[1].plot(y.real, y.imag)
ax[1].set_title('Cercul unitate')
plt.tight_layout()
plt.savefig('Lab3/ex2a.pdf')
plt.show()

# Figura 2
omega = [1, 3, 7, 10]

fig, ax = plt.subplots(2, 2, figsize=(8, 8))
ax = ax.flatten()
for i in range(4):
    z = x * np.exp(-2j*np.pi*omega[i]*n)
    ax[i].plot(z.real, z.imag)
    ax[i].set_title(f'omega = {omega[i]} Hz')
plt.tight_layout()
plt.savefig('Lab3/ex2b.pdf')
plt.show()
