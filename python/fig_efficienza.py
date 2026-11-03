"""
fig_efficienza.py — Capitolo 4, efficienza E(C_L) di una polare parabolica.
Eseguire dalla cartella Libro/:  python3 python/fig_efficienza.py
"""
import math
import matplotlib.pyplot as plt

CD0, AR, e_osw, CLmax = 0.025, 8.0, 0.80, 1.4
k = 1 / (math.pi * e_osw * AR)
CL = [CLmax * i / 400 for i in range(401)]
E = [c / (CD0 + k * c * c) for c in CL]
CLs = math.sqrt(CD0 / k); Es = 1 / (2 * math.sqrt(CD0 * k))

fig, ax = plt.subplots(figsize=(7, 3.2))
ax.plot(CL, E, color="#1F4E79", lw=2)
ax.plot([CLs, CLs], [0, Es], ls="--", color="#5A5A5A", lw=1)
ax.plot([0, CLs], [Es, Es], ls="--", color="#5A5A5A", lw=1)
ax.plot([CLs], [Es], "o", color="#B4662F", ms=6)
ax.annotate(r"$E_{\max}$", (CLs, Es), xytext=(CLs + 0.12, Es + 0.6), fontsize=11)
ax.set_xlabel(r"$C_L$"); ax.set_ylabel(r"$E=C_L/C_D$")
ax.set_xlim(0, CLmax); ax.set_ylim(0, 16)
ax.set_xticks([0, 0.2, 0.4, CLs, 1.0, 1.2, 1.4])
ax.set_xticklabels(["0", "0.2", "0.4", r"$C_L^*$", "1.0", "1.2", r"$C_{L,\max}$"])
ax.grid(alpha=0.25)
for s in ("top", "right"):
    ax.spines[s].set_visible(False)
fig.tight_layout()
fig.savefig("figure/efficienza.png", dpi=220)
