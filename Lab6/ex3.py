import numpy as np
import time

N = 100

p = np.random.randint(-10, 10, N+1)
q = np.random.randint(-10, 10, N+1)

start = time.time()
r_direct = np.zeros(2*N+1)
for i in range(len(p)):
    for j in range(len(q)):
        r_direct[i+j] += p[i] * q[j]
time_direct = time.time() - start

start = time.time()
p_fft = np.fft.fft(p, 2*N+1)
q_fft = np.fft.fft(q, 2*N+1)
r_fft = np.fft.ifft(p_fft * q_fft).real
time_fft = time.time() - start

print(f'Timp direct: {time_direct:.6f} s')
print(f'Timp FFT: {time_fft:.6f} s')
print(f'Dif max: {np.max(np.abs(r_direct - r_fft))}')

# Timp direct: 0.003330 s
# Timp FFT: 0.000070 s
# Dif max: 3.410605131648481e-13
