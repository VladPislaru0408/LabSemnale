import numpy as np
import matplotlib.pyplot as plt

# ex2 - 4 faze diferite pe acelasi grafic
f = 10
t = np.linspace(0, 1, 1000)
faze = [0, np.pi/4, np.pi/2, np.pi]

plt.figure()
for phi in faze:
    plt.plot(t, np.sin(2*np.pi*f*t + phi), label=f'phi={phi:.2f}')
plt.title('Sinusoide cu faze diferite')
plt.savefig('Lab2/ex2a.pdf')
plt.show()

# adaugare zgomot - SNR = ||x||^2 / (gamma^2 * ||z||^2)
x = np.sin(2*np.pi*f*t)
z = np.random.normal(0, 1, len(t))
SNR_vals = [0.1, 1, 10, 100]

fig, ax = plt.subplots(2, 2, figsize=(10, 8))
ax = ax.flatten()

for i, snr in enumerate(SNR_vals):
    # gamma = ||x|| / (sqrt(SNR) * ||z||)
    gamma = np.linalg.norm(x) / (np.sqrt(snr) * np.linalg.norm(z))
    x_zgomot = x + gamma * z
    ax[i].plot(t, x_zgomot)
    ax[i].set_title(f'SNR = {snr}')

plt.tight_layout()
plt.savefig('Lab2/ex2b.pdf')
plt.show()
