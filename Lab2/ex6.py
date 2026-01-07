import numpy as np
import matplotlib.pyplot as plt

# ex6 - frecvente speciale fs/2, fs/4, 0 Hz
fs = 100
t = np.linspace(0, 0.5, 50)  # 50 de esantioane in 0.5 secunde

# a) f = fs/2
x_a = np.sin(2*np.pi*(fs/2)*t)

# b) f = fs/4
x_b = np.sin(2*np.pi*(fs/4)*t)

# c) f = 0 Hz
x_c = np.sin(2*np.pi*0*t)

fig, ax = plt.subplots(3)
ax[0].stem(t, x_a)
ax[0].set_title('f = fs/2')
ax[1].stem(t, x_b)
ax[1].set_title('f = fs/4')
ax[2].stem(t, x_c)
ax[2].set_title('f = 0 Hz')
plt.tight_layout()
plt.savefig('Lab2/ex6.pdf')
plt.show()
