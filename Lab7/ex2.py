import numpy as np
import matplotlib.pyplot as plt
from scipy import datasets

X = datasets.face(gray=True)
snr_threshold = 0.1

def snr(original, compressed):
    mse = np.mean((original - compressed) ** 2)
    if mse == 0:
        return np.inf
    return np.mean(X**2) / mse

Z = X.copy()
for step in range(200):
    current_snr = snr(X, Z)
    print("Step", step, "SNR =", current_snr)
    if current_snr <= snr_threshold:
        break

    Y = np.fft.fft2(Z)
    dc = Y[0, 0]
    Y[0, 0] = 0
    threshold = np.max(np.abs(Y)) * 0.9
    Y[np.abs(Y) >= threshold] *= 0.1
    Y[0, 0] = dc
    Z = np.real(np.fft.ifft2(Y))

plt.subplot(1, 2, 1)
plt.imshow(X, cmap="gray")
plt.title("Original")

plt.subplot(1, 2, 2)
plt.imshow(Z, cmap="gray")
plt.title("Compressed")

plt.show()
