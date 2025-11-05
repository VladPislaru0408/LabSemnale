import numpy as np
import matplotlib.pyplot as plt

# ex2 - demonstrare fenomen aliasing

# frecventa originala si de esantionare
f0 = 12  # Hz
fs_sub = 7  # sub-Nyquist (ar trebui > 24 Hz)

# 3 semnale cu frecvente diferite care produc acelasi esantion
semnal_a = lambda x: np.sin(2*np.pi*f0*x)
semnal_b = lambda x: np.sin(2*np.pi*(f0 + fs_sub)*x)
semnal_c = lambda x: np.sin(2*np.pi*(f0 + 2*fs_sub)*x)

# axe timp
t_continuu = np.linspace(0, 1, 1500)
t_esantioane = np.linspace(0, 1, fs_sub)

# calculare valori
y_a = semnal_a(t_continuu)
y_b = semnal_b(t_continuu)
y_c = semnal_c(t_continuu)

# esantioane
es_a = semnal_a(t_esantioane)
es_b = semnal_b(t_esantioane)
es_c = semnal_c(t_esantioane)

# plotare
fig, ax = plt.subplots(3, 1)

ax[0].plot(t_continuu, y_a, 'b')
ax[0].scatter(t_esantioane, es_a, c='r', s=40)
ax[0].set_title(f'Semnal f={f0} Hz')

ax[1].plot(t_continuu, y_b, 'g')
ax[1].scatter(t_esantioane, es_b, c='r', s=40)
ax[1].set_title(f'Semnal f={f0+fs_sub} Hz')

ax[2].plot(t_continuu, y_c, 'm')
ax[2].scatter(t_esantioane, es_c, c='r', s=40)
ax[2].set_title(f'Semnal f={f0+2*fs_sub} Hz')

plt.tight_layout()
plt.savefig('Lab4/ex2.pdf')
plt.show()
