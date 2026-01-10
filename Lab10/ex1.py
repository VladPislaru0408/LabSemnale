import numpy as np
import matplotlib.pyplot as plt

# ex 1 - seria (ca in lab8)
np.random.seed(42)
n = 1000
x = np.arange(n) / 100
comp_trend = 0.3 * x**2 + 0.8 * x
comp_sezon = 3 * np.cos(2 * np.pi * x / 1.5) + 1.5 * np.sin(2 * np.pi * x / 0.7)
comp_zgomot = np.random.randn(n) * 1.5
semnal = comp_trend + comp_sezon + comp_zgomot

plt.plot(semnal)
plt.savefig('ex1.pdf')
plt.show()

# ex 2 - model AR
p = 50
Y = np.zeros((n-p, p))
for i in range(n-p):
    for j in range(p):
        Y[i][j] = semnal[i+p-1-j]

coef = np.linalg.lstsq(Y, semnal[p:], rcond=None)[0]

pred = np.zeros(n)
pred[:p] = semnal[:p]
for i in range(p, n):
    suma = 0
    for j in range(p):
        suma = suma + coef[j] * semnal[i-1-j]
    pred[i] = suma

plt.plot(semnal, alpha=0.4)
plt.plot(pred)
plt.savefig('ex2.pdf')
plt.show()
print('coef nenuli AR:', np.sum(np.abs(coef) > 0.01))

# ex 3a - AR sparse greedy
best_idx = []
remaining = list(range(p))

for k in range(10):
    best_err = 999999
    best_j = -1
    for j in remaining:
        idx = best_idx + [j]
        Y_sub = Y[:, idx]
        c_sub = np.linalg.lstsq(Y_sub, semnal[p:], rcond=None)[0]
        err = np.sum((Y_sub @ c_sub - semnal[p:])**2)
        if err < best_err:
            best_err = err
            best_j = j
    best_idx.append(best_j)
    remaining.remove(best_j)

Y_greedy = Y[:, best_idx]
coef_greedy_vals = np.linalg.lstsq(Y_greedy, semnal[p:], rcond=None)[0]
coef_greedy = np.zeros(p)
for i in range(len(best_idx)):
    coef_greedy[best_idx[i]] = coef_greedy_vals[i]

pred_greedy = np.zeros(n)
pred_greedy[:p] = semnal[:p]
for i in range(p, n):
    suma = 0
    for j in range(p):
        suma = suma + coef_greedy[j] * semnal[i-1-j]
    pred_greedy[i] = suma

plt.plot(semnal, alpha=0.4)
plt.plot(pred_greedy)
plt.savefig('ex3a.pdf')
plt.show()
print('coef nenuli greedy:', np.sum(np.abs(coef_greedy) > 0.01))

# ex 3b - AR sparse L1 (LASSO cu coordinate descent)
lambd = 5.0
coef_l1 = coef.copy()

for iter in range(100):
    for j in range(p):
        r = semnal[p:] - Y @ coef_l1 + Y[:, j] * coef_l1[j]
        z = Y[:, j] @ r
        norm_j = Y[:, j] @ Y[:, j]
        if z > lambd:
            coef_l1[j] = (z - lambd) / norm_j
        elif z < -lambd:
            coef_l1[j] = (z + lambd) / norm_j
        else:
            coef_l1[j] = 0

pred_l1 = np.zeros(n)
pred_l1[:p] = semnal[:p]
for i in range(p, n):
    suma = 0
    for j in range(p):
        suma = suma + coef_l1[j] * semnal[i-1-j]
    pred_l1[i] = suma

plt.plot(semnal, alpha=0.4)
plt.plot(pred_l1)
plt.savefig('ex3b.pdf')
plt.show()
print('coef nenuli L1:', np.sum(np.abs(coef_l1) > 0.01))

# ex 4 - radacini polinom cu matrice companion
def radacini_polinom(coef_poly):
    m = len(coef_poly)
    companion = np.zeros((m, m))
    for i in range(m):
        companion[0][i] = -coef_poly[i]
    for i in range(1, m):
        companion[i][i-1] = 1
    return np.linalg.eigvals(companion)

# test
print('test x^2 - 5x + 6:', radacini_polinom([-5, 6]))

# ex 5 - stationaritate
def verifica_stationaritate(coef_ar):
    rad = radacini_polinom(coef_ar)
    module = np.abs(rad)
    print('module (min, max):', np.min(module), np.max(module))
    return np.all(module > 1)

print('AR stationar:', verifica_stationaritate(coef))
print('greedy stationar:', verifica_stationaritate(coef_greedy))
print('L1 stationar:', verifica_stationaritate(coef_l1))

# grafic radacini
theta = np.linspace(0, 2*np.pi, 100)
plt.plot(np.cos(theta), np.sin(theta), 'k--')
rad = radacini_polinom(coef)
plt.scatter(np.real(rad), np.imag(rad), alpha=0.5)
plt.axis('equal')
plt.savefig('ex5.pdf')
plt.show()
