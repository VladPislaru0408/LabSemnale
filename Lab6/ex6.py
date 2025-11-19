import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import butter, cheby1, filtfilt

semnal_complet = np.genfromtxt('../Train.csv', delimiter=',', skip_header=1, usecols=2)

x = semnal_complet[:72]

fig1, axes1 = plt.subplots(5, 1, figsize=(12, 12))

axes1[0].plot(x)
axes1[0].set_title('Semnal original (3 zile)')
axes1[0].grid(True)

ferestre = [5, 9, 13, 17]
for idx, w in enumerate(ferestre):
    x_filtrat = np.convolve(x, np.ones(w), 'valid') / w
    axes1[idx+1].plot(x_filtrat)
    axes1[idx+1].set_title(f'Medie alunecatoare w={w}')
    axes1[idx+1].grid(True)

plt.tight_layout()
plt.show()

fs = 1
Ts = 1
f_taiere = 1 / 24
Wn = f_taiere / (fs / 2)

print(f'Frecventa de taiere: {f_taiere} Hz')
print(f'Frecventa normalizata: {Wn}')

b_butter, a_butter = butter(5, Wn, btype='low')
b_cheby, a_cheby = cheby1(5, 5, Wn, btype='low')

x_butter = filtfilt(b_butter, a_butter, x)
x_cheby = filtfilt(b_cheby, a_cheby, x)

fig2, axes2 = plt.subplots(3, 1, figsize=(12, 10))

axes2[0].plot(x, label='Original')
axes2[0].set_title('Semnal original')
axes2[0].legend()
axes2[0].grid(True)

axes2[1].plot(x, alpha=0.5, label='Original')
axes2[1].plot(x_butter, label='Butterworth')
axes2[1].set_title('Filtru Butterworth')
axes2[1].legend()
axes2[1].grid(True)

axes2[2].plot(x, alpha=0.5, label='Original')
axes2[2].plot(x_cheby, label='Chebyshev')
axes2[2].set_title('Filtru Chebyshev')
axes2[2].legend()
axes2[2].grid(True)

plt.tight_layout()
plt.show()

ordine = [3, 5, 7]
fig3, axes3 = plt.subplots(len(ordine), 1, figsize=(12, 10))

for idx, ordin in enumerate(ordine):
    b, a = butter(ordin, Wn, btype='low')
    x_filt = filtfilt(b, a, x)
    axes3[idx].plot(x, alpha=0.5, label='Original')
    axes3[idx].plot(x_filt, label=f'Butterworth ordin {ordin}')
    axes3[idx].set_title(f'Ordin {ordin}')
    axes3[idx].legend()
    axes3[idx].grid(True)

plt.tight_layout()
plt.show()

rp_values = [1, 5, 10]
fig4, axes4 = plt.subplots(len(rp_values), 1, figsize=(12, 10))

for idx, rp in enumerate(rp_values):
    b, a = cheby1(5, rp, Wn, btype='low')
    x_filt = filtfilt(b, a, x)
    axes4[idx].plot(x, alpha=0.5, label='Original')
    axes4[idx].plot(x_filt, label=f'Chebyshev rp={rp} dB')
    axes4[idx].set_title(f'rp = {rp} dB')
    axes4[idx].legend()
    axes4[idx].grid(True)

plt.tight_layout()
plt.show()
