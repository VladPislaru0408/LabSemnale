import numpy as np
import matplotlib.pyplot as plt

N = 64
F = np.zeros((N, N), dtype=complex)

for k in range(N):
    for n in range(N):
        F[k, n] = np.exp(-2j * np.pi * k * n / N)

fig, ax = plt.subplots(6, figsize=(10, 12))
for k in range(6):
    ax[k].plot(range(N), F[k].real, label='Real')
    ax[k].plot(range(N), F[k].imag, label='Imaginar')
    ax[k].set_title(f'Linia {k}')
    ax[k].legend()
plt.tight_layout()
plt.savefig('Lab3/ex1.pdf')
plt.show()

# verificare unitaritate
print(f"Unitara: {np.allclose(F.conj().T @ F, N * np.eye(N))}")
