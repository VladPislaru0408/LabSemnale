import numpy as np
import matplotlib.pyplot as plt

N = 100
x = np.random.rand(N)

x1 = x
x2 = np.convolve(x1, x1)
x3 = np.convolve(x2, x2)
x4 = np.convolve(x3, x3)

fig, axes = plt.subplots(4, 1, figsize=(10, 12))

axes[0].plot(x1)
axes[0].set_title('x1')
axes[0].grid(True)

axes[1].plot(x2)
axes[1].set_title('x2 = x1 * x1')
axes[1].grid(True)

axes[2].plot(x3)
axes[2].set_title('x3 = x2 * x2')
axes[2].grid(True)

axes[3].plot(x4)
axes[3].set_title('x4 = x3 * x3')
axes[3].grid(True)

plt.tight_layout()
plt.show()
