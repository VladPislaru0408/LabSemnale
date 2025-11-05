import numpy as np
import matplotlib.pyplot as plt
from time import perf_counter


# DFT 
def DFT(x):
    N = len(x)
    X = np.zeros(N, dtype=complex)

    for k in range(N):
        for n in range(N):
            X[k] += x[n] * np.exp(-2j * np.pi * k * n / N)

    return X

# FFT - rec
def FFT(x):
    N = len(x)

    if N <= 1:
        return x

    # separare in pare si impare
    pare = FFT(x[0::2])
    impare = FFT(x[1::2])

    T = [np.exp(-2j * np.pi * k / N) * impare[k] for k in range(N // 2)]

    return [pare[k] + T[k] for k in range(N // 2)] + \
           [pare[k] - T[k] for k in range(N // 2)]

# semnal de test
def creeaza_semnal(t):
    return 2*np.sin(2*np.pi*8*t) + 5*np.sin(2*np.pi*16*t) + 3*np.sin(2*np.pi*25*t)

# vectori pentru rrez
N_values = [128, 256, 512, 1024, 2048, 4096, 8192]
t_dft = []
t_fft = []
t_numpy = []


for N in N_values:
    
    t = np.linspace(0, 1, N)
    sig = creeaza_semnal(t)

    # test DFT
    t1 = perf_counter()
    X_dft = DFT(sig)
    t2 = perf_counter()
    t_dft.append((t2-t1)*1000)

    # test FFT
    t1 = perf_counter()
    X_fft = FFT(sig)
    t2 = perf_counter()
    t_fft.append((t2-t1)*1000)

    # test numpy
    t1 = perf_counter()
    X_np = np.fft.fft(sig)
    t2 = perf_counter()
    t_numpy.append((t2-t1)*1000)

    print(f"N={N}: DFT={t_dft[-1]:.2f}ms, FFT={t_fft[-1]:.2f}ms, NumPy={t_numpy[-1]:.2f}ms")

# plot
fig = plt.figure(figsize=(10, 6))
plt.plot(N_values, t_dft, 'r-o', label='DFT')
plt.plot(N_values, t_fft, 'g-s', label='FFT')
plt.plot(N_values, t_numpy, 'b-^', label='NumPy')
plt.yscale('log')
plt.xlabel('N (dimensiune)')
plt.ylabel('Timp (ms)')
plt.title('Comparatie timpi executie')
plt.legend()
plt.grid(True, alpha=0.3)
plt.savefig('Lab4/ex1.pdf')
plt.show()
