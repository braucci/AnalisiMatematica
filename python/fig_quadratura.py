"""
fig_quadratura.py — Capitolo 8, formule di quadratura per exp(-x^2) in [0, 1].
Eseguire dalla cartella Libro/:  python3 python/fig_quadratura.py
"""
import math
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Polygon

blu, rame, grigio, verde = "#1F4E79", "#B4662F", "#5A5A5A", "#2F6B4F"
f = lambda x: np.exp(-x * x)
I = math.erf(1) * math.sqrt(math.pi) / 2

def quadrature(n):
    h = 1 / n
    x = np.linspace(0, 1, n + 1)
    ret = h * f(x[:-1]).sum()
    med = h * f(x[:-1] + h / 2).sum()
    tra = h * (f(x).sum() - (f(0) + f(1)) / 2)
    return ret, med, tra, (2 * med + tra) / 3

fig, axs = plt.subplots(1, 2, figsize=(8.6, 3.5))
ax = axs[0]
n = 4
x = np.linspace(0, 1, n + 1)
for a, b in zip(x[:-1], x[1:]):
    ax.add_patch(Rectangle((a, 0), b - a, f((a + b) / 2), fc="#C9D7E8", ec=blu, lw=0.6))
    ax.add_patch(Polygon([(a, 0), (b, 0), (b, f(b)), (a, f(a))], closed=True,
                         fill=False, ec=rame, lw=1.1))
t = np.linspace(0, 1.05, 200)
ax.plot(t, f(t), color=blu, lw=1.6)
ax.set_title("punto medio e trapezi, $n=4$", fontsize=9)
ax.set_xlim(0, 1.08); ax.set_ylim(0, 1.08)
ax = axs[1]
ns = 2 ** np.arange(1, 9)
E = np.array([[abs(q - I) for q in quadrature(k)] for k in ns])
nomi = ("rettangoli", "punto medio", "trapezi", "Cavalieri-Simpson")
stili = ((grigio, "o-"), (blu, "s-"), (rame, "^-"), (verde, "d-"))
for j, (nome, (col, st)) in enumerate(zip(nomi, stili)):
    ax.loglog(ns, E[:, j], st, color=col, ms=3.5, lw=1.1, label=nome)
ax.set_xlabel("$n$", fontsize=8); ax.set_ylabel("errore", fontsize=8)
ax.set_title("errori in scala logaritmica", fontsize=9)
ax.legend(fontsize=7, frameon=False, loc="lower left")
for ax in axs:
    ax.tick_params(labelsize=7)
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
fig.tight_layout()
fig.savefig("figure/quadratura.png", dpi=220)
