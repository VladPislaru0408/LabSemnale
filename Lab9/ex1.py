import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA

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

# ex 2a - smoothing simplu
best_a = 0
best_err = 999999
for a in np.arange(0.1, 1.0, 0.05):
    s = np.zeros(n)
    s[0] = semnal[0]
    for i in range(1, n):
        s[i] = a*semnal[i] + (1-a)*s[i-1]
    err = 0
    for i in range(n-1):
        err = err + (s[i] - semnal[i+1])**2
    if err < best_err:
        best_err = err
        best_a = a

print('alpha:', best_a)
s = np.zeros(n)
s[0] = semnal[0]
for i in range(1, n):
    s[i] = best_a*semnal[i] + (1-best_a)*s[i-1]

plt.plot(semnal, alpha=0.4)
plt.plot(s)
plt.savefig('ex2a.pdf')
plt.show()

# ex 2b - dublu
best_a = 0
best_b = 0
best_err = 999999
for a in [0.2, 0.4, 0.6, 0.8]:
    for b in [0.2, 0.4, 0.6]:
        lv = np.zeros(n)
        tr = np.zeros(n)
        lv[0] = semnal[0]
        tr[0] = semnal[1] - semnal[0]
        for i in range(1, n):
            lv[i] = a*semnal[i] + (1-a)*(lv[i-1] + tr[i-1])
            tr[i] = b*(lv[i] - lv[i-1]) + (1-b)*tr[i-1]
        pred = lv + tr
        err = 0
        for i in range(n-1):
            err = err + (pred[i] - semnal[i+1])**2
        if err < best_err:
            best_err = err
            best_a = a
            best_b = b
            best_pred = pred

print('dublu:', best_a, best_b)
plt.plot(semnal, alpha=0.4)
plt.plot(best_pred)
plt.savefig('ex2b.pdf')
plt.show()

# ex 2c - triplu
L = 100
a, b, g = 0.4, 0.15, 0.25
lv = np.zeros(n)
tr = np.zeros(n)
sz = np.zeros(n)
lv[0] = semnal[0]
for i in range(L):
    sz[i] = semnal[i] - lv[0]
for i in range(1, n):
    s_prev = sz[i-L] if i >= L else 0
    lv[i] = a*(semnal[i] - s_prev) + (1-a)*(lv[i-1] + tr[i-1])
    tr[i] = b*(lv[i] - lv[i-1]) + (1-b)*tr[i-1]
    sz[i] = g*(semnal[i] - lv[i]) + (1-g)*s_prev

plt.plot(semnal, alpha=0.4)
plt.plot(lv + tr + sz)
plt.savefig('ex2c.pdf')
plt.show()

# ex 3 - MA
q = 20
mu = np.mean(semnal)
eps = semnal - mu
Y = np.zeros((n-q, q))
for i in range(n-q):
    for j in range(q):
        Y[i][j] = eps[i+q-1-j]
theta = np.linalg.lstsq(Y, semnal[q:] - mu, rcond=None)[0]

pred_ma = np.zeros(n)
pred_ma[:q] = mu
for i in range(q, n):
    suma = 0
    for j in range(q):
        suma = suma + theta[j]*eps[i-1-j]
    pred_ma[i] = mu + suma

plt.plot(semnal, alpha=0.4)
plt.plot(pred_ma)
plt.savefig('ex3.pdf')
plt.show()

# ex 4 - ARMA
best_aic = 999999
best_p = 1
best_q = 1
for p in range(1, 21):
    for q in range(1, 21):
        try:
            fit = ARIMA(semnal, order=(p, 0, q)).fit()
            if fit.aic < best_aic:
                best_aic = fit.aic
                best_p = p
                best_q = q
        except:
            pass

print('ARMA:', best_p, best_q)
fit = ARIMA(semnal, order=(best_p, 0, best_q)).fit()
plt.plot(semnal, alpha=0.4)
plt.plot(fit.fittedvalues)
plt.savefig('ex4.pdf')
plt.show()
