import numpy as np
import matplotlib.pyplot as plt

# ex1 - semnale continue si esantionate

# a) simulare axa timp
timp = np.arange(0, 0.03, 0.0005)

# b) creare semnale
x_t = np.cos(520*np.pi*timp + np.pi/3)
y_t = np.cos(280*np.pi*timp - np.pi/3)
z_t = np.cos(120*np.pi*timp + np.pi/3)

# plotare 
fig1, ax1 = plt.subplots(3)
ax1[0].plot(timp, x_t)
ax1[0].set_title('x(t)')
ax1[1].plot(timp, y_t)
ax1[1].set_title('y(t)')
ax1[2].plot(timp, z_t)
ax1[2].set_title('z(t)')
plt.savefig('Lab1/ex1a.pdf')
plt.show()

# c) esantionare la 200 Hz
fs = 200
T = 1/fs
timp_esant = np.arange(0, 0.03, T)

x_n = np.cos(520*np.pi*timp_esant + np.pi/3)
y_n = np.cos(280*np.pi*timp_esant - np.pi/3)
z_n = np.cos(120*np.pi*timp_esant + np.pi/3)

# plotare semnale esantionate
fig2, ax2 = plt.subplots(3)
ax2[0].stem(timp_esant, x_n)
ax2[0].set_title('x[n]')
ax2[1].stem(timp_esant, y_n)
ax2[1].set_title('y[n]')
ax2[2].stem(timp_esant, z_n)
ax2[2].set_title('z[n]')
plt.tight_layout()
plt.savefig('Lab1/ex1b.pdf')
plt.show()
