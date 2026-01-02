import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import dctn, idctn
import imageio.v2 as imageio

Q_jpeg = np.array([[16, 11, 10, 16, 24, 40, 51, 61],
                   [12, 12, 14, 19, 26, 28, 60, 55],
                   [14, 13, 16, 24, 40, 57, 69, 56],
                   [14, 17, 22, 29, 51, 87, 80, 62],
                   [18, 22, 37, 56, 68, 109, 103, 77],
                   [24, 35, 55, 64, 81, 104, 113, 92],
                   [49, 64, 78, 87, 103, 121, 120, 101],
                   [72, 92, 95, 98, 112, 100, 103, 99]])

# 1
def jpeg_compress(img, Q):
    h, w = img.shape
    result = np.zeros_like(img, dtype=float)
    for i in range(0, h-7, 8):
        for j in range(0, w-7, 8):
            block = img[i:i+8, j:j+8]
            dct = dctn(block, norm='ortho')
            quant = Q * np.round(dct / Q)
            result[i:i+8, j:j+8] = idctn(quant, norm='ortho')
    return result

X = imageio.imread('image.png')
if len(X.shape) == 3:
    X = np.dot(X[...,:3], [0.299, 0.587, 0.114]).astype(np.uint8)
X_comp = jpeg_compress(X, Q_jpeg)

plt.figure()
plt.subplot(1, 2, 1)
plt.imshow(X, cmap='gray')
plt.title('Original')
plt.subplot(1, 2, 2)
plt.imshow(X_comp, cmap='gray')
plt.title('JPEG')
plt.tight_layout()
plt.savefig('ex1.pdf')
plt.show()

# 2
def rgb_to_ycbcr(rgb):
    R, G, B = rgb[:,:,0], rgb[:,:,1], rgb[:,:,2]
    Y = 0.299*R + 0.587*G + 0.114*B
    Cb = 128 - 0.168736*R - 0.331264*G + 0.5*B
    Cr = 128 + 0.5*R - 0.418688*G - 0.081312*B
    return np.stack([Y, Cb, Cr], axis=2)

def ycbcr_to_rgb(ycbcr):
    Y, Cb, Cr = ycbcr[:,:,0], ycbcr[:,:,1], ycbcr[:,:,2]
    R = Y + 1.402*(Cr - 128)
    G = Y - 0.344136*(Cb - 128) - 0.714136*(Cr - 128)
    B = Y + 1.772*(Cb - 128)
    return np.clip(np.stack([R, G, B], axis=2), 0, 255).astype(np.uint8)

def jpeg_color(rgb, Q):
    ycbcr = rgb_to_ycbcr(rgb)
    h, w = ycbcr.shape[:2]
    result = np.zeros_like(ycbcr, dtype=float)
    for c in range(3):
        for i in range(0, h-7, 8):
            for j in range(0, w-7, 8):
                block = ycbcr[i:i+8, j:j+8, c]
                dct = dctn(block, norm='ortho')
                quant = Q * np.round(dct / Q)
                result[i:i+8, j:j+8, c] = idctn(quant, norm='ortho')
    return ycbcr_to_rgb(result)

X_color = imageio.imread('image.png')
X_color_comp = jpeg_color(X_color, Q_jpeg)

plt.figure()
plt.subplot(1, 2, 1)
plt.imshow(X_color)
plt.title('Original')
plt.subplot(1, 2, 2)
plt.imshow(X_color_comp)
plt.title('JPEG color')
plt.tight_layout()
plt.savefig('ex2.pdf')
plt.show()

# 3
def mse(a, b):
    return np.mean((a - b)**2)

def jpeg_mse(img, Q_base, target):
    for scale in np.linspace(0.1, 10, 50):
        Q = np.maximum(1, (Q_base * scale).astype(int))
        comp = jpeg_compress(img, Q)
        if mse(img, comp) <= target:
            return comp
    return img

X_mse = jpeg_mse(X, Q_jpeg, 100)

plt.figure()
plt.subplot(1, 2, 1)
plt.imshow(X, cmap='gray')
plt.title('Original')
plt.subplot(1, 2, 2)
plt.imshow(X_mse, cmap='gray')
plt.title('MSE < 100')
plt.tight_layout()
plt.savefig('ex3.pdf')
plt.show()

# jpeg_video('input.mp4', Q_jpeg, 'output.mp4')
