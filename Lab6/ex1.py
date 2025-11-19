import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-3, 3, 1000)
B = 2.0
y = np.sinc(B * x) ** 2

frequencies = [1, 1.5, 2, 4]

fig, axes = plt.subplots(2, 2, figsize=(14, 10))
axes = axes.flatten()

for idx, fr in enumerate(frequencies):
    ax = axes[idx]
    dt = 1 / fr

    sampled_x_pos = np.arange(0, 3 + dt, dt)
    sampled_x_neg = np.arange(-dt, -3 - dt, -dt)
    sampled_x = np.concatenate((sampled_x_neg[::-1], sampled_x_pos))

    sampled_y = np.sinc(B * sampled_x) ** 2

    reconstructed_signal = np.zeros_like(x)
    for i, point in enumerate(sampled_x):
        reconstructed_signal += np.sinc(((x - point) / dt)) * sampled_y[i]

    ax.plot(x, y, label='x(t) continuu')
    ax.plot(sampled_x, sampled_y, 'ro', markersize=8, label=f'x[n] esantionat')
    ax.plot(x, reconstructed_signal, 'g--', label='x(t) reconstruit')

    ax.set_xlabel('t (secunde)')
    ax.set_ylabel('x(t) = sinc^2(t)')
    ax.set_title(f'fs = {fr} Hz (Ts = {dt:.3f} s)', fontweight='bold')
    ax.legend()
    ax.axhline(y=0, color='k', linewidth=0.5)
    ax.axvline(x=0, color='k', linewidth=0.5)
    ax.set_xlim(-3, 3)

fig.suptitle('Functia x(t) = sinc^2(t) esantionata la diferite frecvente', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.show()
