import numpy as np
import matplotlib.pyplot as plt

# ex3 - fara aliasing cu frecventa Nyquist

# folosim aceleasi semnale ca la ex2
frecv_baza = 12
fs_sub = 7

# calculam frecventa maxima din cele 3 semnale
f_max = frecv_baza + 2*fs_sub  # = 26 Hz
# teorema Nyquist: fs >= 2*f_max = 52 Hz
frecv_esant_nyquist = 80  # alegem 80 Hz

# cele 3 semnale
def semnal_1(x):
    return np.sin(2*np.pi*frecv_baza*x)

def semnal_2(x):
    return np.sin(2*np.pi*(frecv_baza + fs_sub)*x)

def semnal_3(x):
    return np.sin(2*np.pi*(frecv_baza + 2*fs_sub)*x)

# axa de timp pentru plotare continua
t_plot = np.linspace(0, 1, 1800)

# punctele de esantionare
nr_esant = frecv_esant_nyquist
t_esant = np.linspace(0, 1, nr_esant)

# calculez valorile pentru plot
y1_continuu = np.vectorize(semnal_1)(t_plot)
y2_continuu = np.vectorize(semnal_2)(t_plot)
y3_continuu = np.vectorize(semnal_3)(t_plot)

y1_esant = np.vectorize(semnal_1)(t_esant)
y2_esant = np.vectorize(semnal_2)(t_esant)
y3_esant = np.vectorize(semnal_3)(t_esant)

# creez figura
figura, axe = plt.subplots(3, 1)

# primul subplot
axe[0].plot(t_plot, y1_continuu, color='cyan', linewidth=1.5)
axe[0].scatter(t_esant, y1_esant, color='black', s=12)
axe[0].grid(alpha=0.3)

# al doilea subplot
axe[1].plot(t_plot, y2_continuu, color='purple', linewidth=1.5)
axe[1].scatter(t_esant, y2_esant, color='black', s=12)
axe[1].grid(alpha=0.3)

# al treilea subplot
axe[2].plot(t_plot, y3_continuu, color='brown', linewidth=1.5)
axe[2].scatter(t_esant, y3_esant, color='black', s=12)
axe[2].grid(alpha=0.3)

plt.tight_layout()
plt.savefig('Lab4/ex3.pdf')
plt.show()
