import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)
n = 1000
x = np.arange(n) / 100

# a) Componente
comp_trend = 0.3 * x**2 + 0.8 * x
comp_sezon = 3 * np.cos(2 * np.pi * x / 1.5) + 1.5 * np.sin(2 * np.pi * x / 0.7)
comp_zgomot = np.random.randn(n) * 1.5
semnal = comp_trend + comp_sezon + comp_zgomot

fig, ax = plt.subplots(4, 1, figsize=(12, 9), sharex=True)
titluri = ['Componenta Trend', 'Componenta Sezoniera', 'Zgomot Gaussian', 'Semnal Total']
date = [comp_trend, comp_sezon, comp_zgomot, semnal]
culori = ['steelblue', 'coral', 'gray', 'darkgreen']
for i in range(4):
    ax[i].plot(x, date[i], color=culori[i], lw=0.8)
    ax[i].set_ylabel(titluri[i])
ax[-1].set_xlabel('Timp')
plt.tight_layout()
plt.savefig('ex1a.pdf')
plt.show()

# b) Functie autocorelatie
def calculeaza_autocorelatie(s):
    s_norm = s - s.mean()
    corr = np.correlate(s_norm, s_norm, 'full')
    return corr[len(s)-1:] / corr[len(s)-1]

ac = calculeaza_autocorelatie(semnal)
plt.figure(figsize=(10, 4))
plt.stem(ac[:100], linefmt='b-', markerfmt='bo', basefmt=' ')
plt.xlabel('Decalaj')
plt.ylabel('Autocorelatie')
plt.title('Functia de autocorelatie')
plt.savefig('ex1b.pdf')
plt.show()

# c) Functie model AR
def model_ar(serie, ord_p):
    mat = np.column_stack([serie[ord_p-1-k:n-1-k] for k in range(ord_p)])
    tinta = serie[ord_p:]
    phi, *_ = np.linalg.lstsq(mat, tinta, rcond=None)
    return phi, mat

ord_p = 200
phi, mat = model_ar(semnal, ord_p)

# Predictie pas cu pas
rez = semnal.copy()
for t in range(ord_p, n):
    rez[t] = phi @ rez[t-ord_p:t][::-1]

plt.figure(figsize=(12, 5))
plt.plot(x, semnal, 'b', alpha=0.7, label='Date reale')
plt.plot(x, rez, 'r--', alpha=0.8, label=f'Model AR({ord_p})')
plt.xlabel('Timp')
plt.legend()
plt.savefig('ex1c.pdf')
plt.show()

# d) Cautare parametri optimi
def evalueaza(serie, p_test, dim_antren):
    if dim_antren <= p_test:
        return np.inf
    mat_tr = np.column_stack([serie[p_test-1-k:dim_antren-1-k] for k in range(p_test)])
    phi_tr, *_ = np.linalg.lstsq(mat_tr, serie[p_test:dim_antren], rcond=None)

    erori = []
    for t in range(dim_antren, len(serie)):
        pred = phi_tr @ serie[t-p_test:t][::-1]
        erori.append((serie[t] - pred)**2)
    return np.mean(erori) if erori else np.inf

candidati_p = [15, 30, 60, 100]
candidati_m = [200, 400, 600, 800]

rezultate = [(evalueaza(semnal, p, m), p, m) for p in candidati_p for m in candidati_m]
eroare_min, p_opt, m_opt = min(rezultate)

print(f'Parametri optimi: p={p_opt}, m={m_opt}')
print(f'Eroare MSE: {eroare_min:.3f}')
