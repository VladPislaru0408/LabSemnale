import numpy as np
import matplotlib.pyplot as plt

# Citire date
data = np.genfromtxt('Train.csv', delimiter=',', skip_header=1)
x = data[:, 2]
N = len(x)

# (a) Frecventa de esantionare
T = 3600  # secunde
Fs = 1 / T

print("(a) Fs =", Fs, "Hz")

# (b) Intervalul de timp
durata_ore = N * T / 3600
durata_zile = durata_ore / 24

print("(b) Durata:", durata_zile, "zile")

# (c) Frecventa maxima
f_max = Fs / 2

print("(c) f_max =", f_max, "Hz")

# Transformata Fourier
X = np.fft.fft(x)
X_mag = np.abs(X / N)
X_mag = X_mag[:N//2]

# (d) Componenta continua
print("(d) Media =", np.mean(x))
print("    Magnitudine DC =", X_mag[0])

x_fara_DC = x - np.mean(x)
X_fara_DC = np.fft.fft(x_fara_DC)
X_mag_fara_DC = np.abs(X_fara_DC / N)
X_mag_fara_DC = X_mag_fara_DC[:N//2]

# Vector frecvente
f = Fs * np.linspace(0, N//2, N//2) / N

# (e) Frecventele principale
idx_top4 = np.argsort(X_mag[1:])[-4:][::-1] + 1

print("(e) Top 4 frecvente:")
for i in range(4):
    idx = idx_top4[i]
    print("   ", f[idx], "Hz, mag =", X_mag[idx])

# Grafice
fig, axes = plt.subplots(2, 2, figsize=(12, 8))

axes[0,0].plot(x[:500])
axes[0,0].set_title('Semnal Original')
axes[0,0].grid(True)

axes[0,1].plot(x_fara_DC[:500])
axes[0,1].set_title('Semnal fara DC')
axes[0,1].grid(True)

axes[1,0].plot(f[1:200], X_mag[1:200])
axes[1,0].set_title('FFT Original')
axes[1,0].grid(True)

axes[1,1].plot(f[1:200], X_mag_fara_DC[1:200])
axes[1,1].set_title('FFT fara DC')
axes[1,1].grid(True)

plt.tight_layout()
plt.savefig('Lab5/exercitiul1.pdf')
plt.show()

# (f) O luna de trafic
start = 1056
end = start + 720

x_luna = x[start:end]

fig2, ax = plt.subplots(figsize=(12, 5))
ax.plot(x_luna)
ax.set_title('O luna de trafic')
ax.grid(True)
plt.savefig('Lab5/exercitiul5.pdf')
plt.show()

# Metoda determinare data:
# 1. Identificare sarbatori legale
#   - Cautam in semnal zile cu trafic extrem de scazut (mult sub medie)
#   - Sarbatorile majore (Craciun, Anul Nou, Paste) au trafic foarte redus
#   - Acestea au date fixe sau semi-fixe in calendar

#   2. Matching cu calendarul
#   - Odata gasite 2-3 sarbatori in semnal, stim distanta in zile intre ele
#   - Comparam cu calendar: daca gasim Craciun (25 dec) → Anul Nou (1 ian) = 7 zile
#   - Identificam anul si luna analizand pattern-ul de sarbatori

#   3. Numarare inversa
#   - De la sarbatoarea identificata, numaram inapoi pana la primul esantion
#   - Determinam data exacta de start

#   NEAJUNSURI:

#   - Depinde de prezenta sarbatorilor in perioada masurata
#   - Daca datele incep dupa o sarbatoare majora, metoda esueaza
#   - Traficul de sarbatori poate varia (unii calatoresc mai mult, nu mai putin)
#   - Sarbatorile mobile (Pastele) complica identificarea anului

#   FACTORI DE ACURATETE:

#   - Cate sarbatori distincte putem identifica
#   - Cat de evident este drop-ul de trafic in sarbatori
#   - Lungimea totala a semnalului (mai lung = mai multe sarbatori)
#   - Cunostinte despre tara/sistemul feroviar analizat

# (h) Filtrare
f_cutoff = 1 / (24 * 3600)
idx_cutoff = int(f_cutoff * N / Fs)

X_filtrat = X_fara_DC.copy()
X_filtrat[idx_cutoff:-idx_cutoff] = 0
x_filtrat = np.fft.ifft(X_filtrat).real

print("(h) f_cutoff =", f_cutoff, "Hz")

fig3, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 7))

ax1.plot(x_fara_DC[:720], alpha=0.6)
ax1.plot(x_filtrat[:720], linewidth=2)
ax1.set_title('30 zile')
ax1.grid(True)

ax2.plot(x_fara_DC[:168], alpha=0.6)
ax2.plot(x_filtrat[:168], linewidth=2)
ax2.set_title('7 zile')
ax2.grid(True)

plt.tight_layout()
plt.savefig('Lab5/exercitiul7.pdf')
plt.show()
