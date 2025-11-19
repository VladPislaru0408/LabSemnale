import numpy as np
import matplotlib.pyplot as plt

n = 20
x = np.sin(np.linspace(0, 2*np.pi, n))

d = 5
y = np.roll(x, d)

X = np.fft.fft(x)
Y = np.fft.fft(y)

result1 = np.fft.ifft(X * Y).real
result2 = np.fft.ifft(Y / X).real

fig, axes = plt.subplots(4, 1, figsize=(10, 12))

axes[0].stem(x)
axes[0].set_title('x original')
axes[0].grid(True)

axes[1].stem(y)
axes[1].set_title(f'y deplasat cu d={d}')
axes[1].grid(True)

axes[2].stem(result1)
axes[2].set_title('IFFT(FFT(x) * FFT(y))')
axes[2].grid(True)

axes[3].stem(result2)
axes[3].set_title('IFFT(FFT(y) / FFT(x))')
axes[3].grid(True)

plt.tight_layout()
plt.show()

print(f'Deplasare originala: {d}')
print(f'Pozitia maximului in result2: {np.argmax(result2)}')
