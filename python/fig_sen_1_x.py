"""
fig_sen_1_x.py — Capitolo 4, i grafici di sen(1/x) e di x sen(1/x).
Eseguire dalla cartella Libro/:  python3 python/fig_sen_1_x.py
"""
import numpy as np
import matplotlib.pyplot as plt

# campionamento uniforme in t = 1/x: così le oscillazioni vicino a 0 sono risolte
t = np.linspace(1 / 0.6, 400, 400000)
rami = (-1 / t, 1 / t[::-1])           # x < 0 e x > 0, disegnati separatamente

fig, (a1, a2) = plt.subplots(1, 2, figsize=(8, 3.0))
for x in rami:
    a1.plot(x, np.sin(1 / x), color="#1F4E79", lw=0.5)
a1.set_title(r"$y=\mathrm{sen}\,(1/x)$", fontsize=11)
a1.set_ylim(-1.3, 1.3)
z = np.array([-0.6, 0, 0.6])
a2.plot(z, np.abs(z), "--", color="#5A5A5A", lw=1)
a2.plot(z, -np.abs(z), "--", color="#5A5A5A", lw=1)
for x in rami:
    a2.plot(x, x * np.sin(1 / x), color="#B4662F", lw=0.6)
a2.set_title(r"$y=x\,\mathrm{sen}\,(1/x)$  e  $y=\pm|x|$", fontsize=11)
a2.set_ylim(-0.65, 0.65)
for ax in (a1, a2):
    ax.set_xlim(-0.6, 0.6)
    ax.axhline(0, color="black", lw=0.6); ax.axvline(0, color="black", lw=0.6)
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
fig.tight_layout()
fig.savefig("figure/sen_1_x.png", dpi=220)
