"""
fig_infiniti.py — Capitolo 3, gerarchia degli infiniti in scala logaritmica.
Eseguire dalla cartella Libro/:  python3 python/fig_infiniti.py
"""
import math
import matplotlib.pyplot as plt

n = list(range(2, 31))
# colori della palette del libro; n^n si distingue da 2^n per tratto e marcatore
serie = [
    (r"$\log n$", [math.log(k) for k in n], "#2F6B4F", "o-"),
    (r"$n^2$",    [k**2 for k in n], "#5A5A5A", "o-"),
    (r"$2^n$",    [2.0**k for k in n], "#1F4E79", "o-"),
    (r"$n!$",     [float(math.factorial(k)) for k in n], "#B4662F", "o-"),
    (r"$n^n$",    [float(k)**k for k in n], "#1F4E79", "s--"),
]
fig, ax = plt.subplots(figsize=(7, 3.8))
for nome, valori, colore, stile in serie:
    ax.semilogy(n, valori, stile, ms=3, lw=1.2, color=colore, label=nome)
ax.set_xlabel(r"$n$"); ax.set_xlim(1, 31)
ax.legend(frameon=False, ncol=5, loc="upper left")
ax.grid(alpha=0.25, which="both")
for s in ("top", "right"):
    ax.spines[s].set_visible(False)
fig.tight_layout()
fig.savefig("figure/infiniti.png", dpi=220)
