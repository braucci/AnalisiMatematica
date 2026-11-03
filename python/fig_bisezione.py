"""
fig_bisezione.py — Capitolo 4, gli intervalli incapsulati del metodo di bisezione.
Eseguire dalla cartella Libro/:  python3 python/fig_bisezione.py
"""
import numpy as np
import matplotlib.pyplot as plt

f = lambda x: x**3 + x - 1
a, b = 0.0, 1.0
intervalli = [(a, b)]
for _ in range(5):
    c = (a + b) / 2
    if f(c) > 0:
        b = c
    else:
        a = c
    intervalli.append((a, b))

x = np.linspace(-0.05, 1.08, 400)
fig, ax = plt.subplots(figsize=(7, 3.8))
ax.axhline(0, color="black", lw=0.7)
ax.plot(x, f(x), color="#1F4E79", lw=2, label=r"$f(x)=x^3+x-1$")
for k, (p, q) in enumerate(intervalli):
    y = -1.25 - 0.18 * k
    ax.plot([p, q], [y, y], color="#B4662F", lw=3, solid_capstyle="butt")
    ax.text(-0.04, y, rf"$[a_{k},b_{k}]$" if k else r"$[a,b]$", va="center",
            ha="right", fontsize=9)
x0 = 0.6823278038
ax.axvline(x0, color="#5A5A5A", ls=":", lw=1)
ax.plot([x0], [0], "o", color="#B4662F", ms=5)
ax.annotate(r"$x_0$", (x0, 0), xytext=(x0 + 0.03, 0.18), fontsize=11)
ax.set_xlim(-0.2, 1.1); ax.set_ylim(-2.25, 1.2)
ax.set_yticks([-1, 0, 1])
ax.legend(frameon=False, loc="upper left")
for s in ("top", "right"):
    ax.spines[s].set_visible(False)
fig.tight_layout()
fig.savefig("figure/bisezione.png", dpi=220)
