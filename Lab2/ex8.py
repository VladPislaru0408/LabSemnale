import numpy as np
import matplotlib.pyplot as plt

# ex8 - aproximare sin(alpha) pentru valori mici
alpha = np.linspace(-np.pi/2, np.pi/2, 1000)

sin_exact = np.sin(alpha)
taylor = alpha  # sin(a) aprox a
pade = (alpha - 7*alpha**3/60) / (1 + alpha**2/20)

# grafic comparatie
plt.plot(alpha, sin_exact, label='sin(alfa)')
plt.plot(alpha, taylor, '--', label='Taylor: alfa')
plt.plot(alpha, pade, ':', label='Pade')
plt.title('Comparatie sin(alfa) cu aproximari')
plt.savefig('Lab2/ex8a.pdf')
plt.show()
