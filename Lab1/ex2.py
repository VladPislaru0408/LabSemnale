import numpy as np
import matplotlib.pyplot as plt

# ex2 - generare diverse tipuri de semnale

# a) sinusoida 400 Hz cu 1600 esantioane
f_a = 400
N_a = 1600
# pentru 1600 de esantioane la 400 Hz trebuie sa calculam durata
# daca vrem sa capturam mai multe perioade complete
fs_a = 1600  # esantioane pe secunda (arbitrar ales)
t_a = np.arange(N_a) / fs_a
semnal_a = np.sin(2*np.pi*f_a*t_a)

plt.figure()
plt.plot(t_a, semnal_a)
plt.title('Sinusoida 400Hz, 1600 esantioane')
plt.xlabel('Timp (s)')
plt.ylabel('Amplitudine')
plt.savefig('Lab1/ex2a.pdf')
plt.show()

# b) sinusoida 800 Hz, durata 3 sec
f_b = 800
durata = 3
fs_b = 8000  # frecventa de esantionare
N_b = int(durata * fs_b)
t_b = np.linspace(0, durata, N_b)
semnal_b = np.sin(2*np.pi*f_b*t_b)

plt.figure()
plt.plot(t_b, semnal_b)
plt.title('Sinusoida 800Hz, 3 secunde')
plt.xlabel('Timp (s)')
plt.ylabel('Amplitudine')
plt.savefig('Lab1/ex2b.pdf')
plt.show()

# c) sawtooth 240 Hz
f_c = 240
durata_c = 0.1  # 100ms pentru vizualizare
fs_c = 10000
t_c = np.linspace(0, durata_c, int(durata_c*fs_c))
semnal_c = 2 * (f_c*t_c - np.floor(0.5 + f_c*t_c))

plt.figure()
plt.plot(t_c, semnal_c)
plt.title('Sawtooth 240Hz')
plt.xlabel('Timp (s)')
plt.ylabel('Amplitudine')
plt.savefig('Lab1/ex2c.pdf')
plt.show()

# d) square 300 Hz
f_d = 300
durata_d = 0.05
fs_d = 10000
t_d = np.linspace(0, durata_d, int(durata_d*fs_d))
semnal_d = np.sign(np.sin(2*np.pi*f_d*t_d))

plt.figure()
plt.plot(t_d, semnal_d)
plt.title('Square 300Hz')
plt.xlabel('Timp (s)')
plt.ylabel('Amplitudine')
plt.ylim(-1.5, 1.5)
plt.savefig('Lab1/ex2d.pdf')
plt.show()

# e) imagine aleatoare 128x128
img_random = np.random.rand(128, 128)

plt.figure()
plt.imshow(img_random, cmap='gray')
plt.title('Imagine aleatoare')
plt.colorbar()
plt.savefig('Lab1/ex2e.pdf')
plt.show()

# f) imagine custom - pattern circular
img_custom = np.zeros((128, 128))
centru = 64
for i in range(128):
    for j in range(128):
        dist = np.sqrt((i-centru)**2 + (j-centru)**2)
        if dist < 50 and dist > 30:
            img_custom[i,j] = 1

plt.figure()
plt.imshow(img_custom, cmap='gray')
plt.title('Pattern circular')
plt.savefig('Lab1/ex2f.pdf')
plt.show()
