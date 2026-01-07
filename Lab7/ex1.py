import numpy as np
import matplotlib.pyplot as plt

n1, n2 = 64, 64
i, j = np.indices((n1, n2))

# 1.1 sin(2*pi*n1 + 3*pi*n2)
x = np.sin(2 * np.pi * i + 3 * np.pi * j)
Y = 20 * np.log10(abs(np.fft.fft2(x)) + 1e-10)

plt.subplot(1, 2, 1)
plt.imshow(x)
plt.title("Functia")
plt.subplot(1, 2, 2)
plt.imshow(Y)
plt.title("Spectrul")
plt.savefig('ex1a.pdf')
plt.show()

# 1.2 sin(4*pi*n1) + cos(6*pi*n2)
x = np.sin(4 * np.pi * i) + np.cos(6 * np.pi * j)
Y = 20 * np.log10(abs(np.fft.fft2(x)) + 1e-10)

plt.subplot(1, 2, 1)
plt.imshow(x)
plt.title("Functia")
plt.subplot(1, 2, 2)
plt.imshow(Y)
plt.title("Spectrul")
plt.savefig('ex1b.pdf')
plt.show()

# 1.3 Y[0,5] = Y[0,N-5] = 1
Y = np.zeros((n1, n2))
Y[0, 5] = 1
Y[0, -5] = 1
x = np.fft.ifft2(Y)

plt.subplot(1, 2, 1)
plt.imshow(np.real(x))
plt.title("Functia")
plt.subplot(1, 2, 2)
plt.imshow(Y)
plt.title("Spectrul")
plt.savefig('ex1c.pdf')
plt.show()

# 1.4 Y[5,0] = Y[N-5,0] = 1
Y = np.zeros((n1, n2))
Y[5, 0] = 1
Y[-5, 0] = 1
x = np.fft.ifft2(Y)

plt.subplot(1, 2, 1)
plt.imshow(np.real(x))
plt.title("Functia")
plt.subplot(1, 2, 2)
plt.imshow(Y)
plt.title("Spectrul")
plt.savefig('ex1d.pdf')
plt.show()

# 1.5 Y[5,5] = Y[N-5,N-5] = 1
Y = np.zeros((n1, n2))
Y[5, 5] = 1
Y[-5, -5] = 1
x = np.fft.ifft2(Y)

plt.subplot(1, 2, 1)
plt.imshow(np.real(x))
plt.title("Functia")
plt.subplot(1, 2, 2)
plt.imshow(Y)
plt.title("Spectrul")
plt.savefig('ex1e.pdf')
plt.show()
