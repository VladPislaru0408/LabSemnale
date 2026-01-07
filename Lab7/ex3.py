import numpy as np
import matplotlib.pyplot as plt
from scipy import datasets, ndimage

X = datasets.face(gray=True)

pixel_noise = 200
noise = np.random.randint(-pixel_noise, high=pixel_noise + 1, size=X.shape)
X_noisy = X + noise

def snr(original, modified):
    mse = np.mean((original - modified) ** 2)
    return np.mean(original**2) / mse

print("SNR inainte:", snr(X, X_noisy))

# filtru gaussian
Y_noisy = np.fft.fftshift(np.fft.fft2(X_noisy))

h, w = Y_noisy.shape
sigma = 50
filtru = np.zeros((h, w))
for i in range(h):
    for j in range(w):
        filtru[i, j] = np.exp(-((i - h//2)**2 + (j - w//2)**2) / (2 * sigma**2))

Y_filtrat = Y_noisy * filtru
X_filtrat = np.real(np.fft.ifft2(np.fft.ifftshift(Y_filtrat)))

print("SNR dupa:", snr(X, X_filtrat))

plt.subplot(1, 3, 1)
plt.imshow(X, cmap="gray")
plt.title("Original")

plt.subplot(1, 3, 2)
plt.imshow(X_noisy, cmap="gray")
plt.title("Noisy")

plt.subplot(1, 3, 3)
plt.imshow(X_filtrat, cmap="gray")
plt.title("Filtrat")

plt.savefig('ex3.pdf')
plt.show()
