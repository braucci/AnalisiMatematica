"""
fig_funzione_integrale.py — Capitolo 9, la funzione integrale di exp(-t^2).
Eseguire dalla cartella Libro/:  python3 python/fig_funzione_integrale.py
"""
import math
import numpy as np
import matplotlib.pyplot as plt

blu, rame, grigio = "#1F4E79", "#B4662F", "#5A5A5A"
t = np.linspace(-3, 3, 600)
f = np.exp(-t**2)
F = np.array([math.sqrt(math.pi) / 2 * math.erf(v) for v in t])
x0 = 1.0
F0 = math.sqrt(math.pi) / 2 * math.erf(x0)

fig, axs = plt.subplots(2, 1, figsize=(8.6, 4.8), sharex=True)
ax = axs[0]
ax.plot(t, f, color=blu, lw=1.6)
m = (t >= 0) & (t <= x0)
ax.fill_between(t[m], f[m], color="#C9D7E8")
ax.text(0.45, 0.35, "$F(1)$", color=blu, fontsize=9, ha="center")
ax.set_ylabel("$f(t)=e^{-t^2}$", fontsize=8)
ax.set_ylim(0, 1.1)
ax = axs[1]
ax.plot(t, F, color=blu, lw=1.6)
for y in (math.sqrt(math.pi) / 2, -math.sqrt(math.pi) / 2):
    ax.axhline(y, color=grigio, lw=0.7, ls="--")
s = np.linspace(x0 - 1.0, x0 + 1.0, 10)
ax.plot(s, F0 + math.exp(-x0**2) * (s - x0), color=rame, lw=1.2)
ax.plot(x0, F0, "o", color=rame, ms=4)
ax.plot(0, 0, "o", color=grigio, ms=3)
ax.text(1.25, 0.55, "pendenza $f(1)=e^{-1}$", color=rame, fontsize=8)
ax.text(-2.9, 0.95, r"$\sqrt{\pi}/2$", color=grigio, fontsize=8)
ax.set_ylabel(r"$F(x)=\int_0^x e^{-t^2}dt$", fontsize=8)
ax.set_xlabel("$x$", fontsize=8)
for ax in axs:
    ax.tick_params(labelsize=7)
    for sp_ in ("top", "right"):
        ax.spines[sp_].set_visible(False)
fig.tight_layout()
fig.savefig("figure/funzione_integrale.png", dpi=220)
