import numpy as np
import matplotlib.pyplot as plt

# ex7 - decimare semnal
fs = 500
f = 50
t = np.linspace(0, 0.1, 100)
x = np.sin(2*np.pi*f*t)

# a) pastram 0,4,8,...
x_dec = x[::4]
t_dec = t[::4]

fig, ax = plt.subplots(2)
ax[0].plot(t, x)
ax[0].set_title('Semnal original')
ax[1].stem(t_dec, x_dec)
ax[1].set_title('Semnal decimat (1/4)')
plt.tight_layout()
plt.savefig('Lab2/ex7a.pdf')
plt.show()

# b) pastram 1,5,9,...
x_dec2 = x[1::4]
t_dec2 = t[1::4]

fig, ax = plt.subplots(2)
ax[0].stem(t_dec, x_dec)
ax[0].set_title('Decimat de la elem 0')
ax[1].stem(t_dec2, x_dec2)
ax[1].set_title('Decimat de la elem 1')
plt.tight_layout()
plt.savefig('Lab2/ex7b.pdf')
plt.show()
