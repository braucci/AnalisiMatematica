"""
fig_resistenza_potenza.py — Capitolo 6, resistenza e potenza necessaria in volo livellato.
Eseguire dalla cartella Libro/:  python3 python/fig_resistenza_potenza.py
"""
import math
import numpy as np
import matplotlib.pyplot as plt

blu, rame, grigio = "#1F4E79", "#B4662F", "#5A5A5A"
W, S, rho, CD0, AR, e = 10000.0, 16.0, 1.225, 0.025, 8.0, 0.8
k = 1 / (math.pi * e * AR)
a, b = 0.5 * rho * S * CD0, 2 * k * W**2 / (rho * S)
V = np.linspace(12, 80, 800)
VD, VP = (b / a) ** 0.25, (b / (3 * a)) ** 0.25

fig, axs = plt.subplots(1, 2, figsize=(8.6, 3.3))
ax = axs[0]
ax.plot(V, a * V**2, "--", color=grigio, lw=0.9, label=r"parassita $aV^2$")
ax.plot(V, b / V**2, ":", color=grigio, lw=1.1, label=r"indotta $b/V^2$")
ax.plot(V, a * V**2 + b / V**2, color=blu, lw=1.8, label=r"$D(V)$")
DD = a * VD**2 + b / VD**2
ax.plot([VD, VD], [0, DD], color=rame, lw=0.8)
ax.plot([VD], [DD], "o", color=rame, ms=4)
ax.annotate(f"$V_{{\\min D}}\\approx{VD:.1f}$ m/s".replace(".", "{,}"),
            (VD, DD), (VD + 6, DD + 900), fontsize=8, color=rame,
            arrowprops=dict(arrowstyle="-", color=rame, lw=0.6))
ax.set_ylim(0, 3000); ax.set_ylabel("resistenza (N)", fontsize=8)
ax.legend(fontsize=7.5, frameon=False, loc="upper center")
ax = axs[1]
P = (a * V**2 + b / V**2) * V / 1000
ax.plot(V, P, color=blu, lw=1.8, label=r"$P(V)=D(V)\,V$")
for Vs, lab, dx, al in ((VP, r"V_{\min P}", -0.8, "right"),
                       (VD, r"V_{\min D}", 0.8, "left")):
    Ps = (a * Vs**2 + b / Vs**2) * Vs / 1000
    ax.plot([Vs, Vs], [0, Ps], color=rame, lw=0.8)
    ax.plot([Vs], [Ps], "o", color=rame, ms=4)
    ax.text(Vs + dx, 4, f"${lab}$", fontsize=8, color=rame, ha=al)
# la tangente per l'origine tocca P(V) in V_minD: P/V = D minima
ax.plot([0, 80], [0, 80 * DD / 1000], "--", color=grigio, lw=0.8)
ax.text(63, 29, "tangente\nper l'origine", fontsize=7.5, color=grigio)
ax.set_ylim(0, 100); ax.set_ylabel("potenza (kW)", fontsize=8)
ax.legend(fontsize=7.5, frameon=False, loc="upper center")
for ax in axs:
    ax.set_xlim(0, 80); ax.set_xlabel("velocità $V$ (m/s)", fontsize=8)
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
    ax.tick_params(labelsize=7.5)
fig.tight_layout()
fig.savefig("figure/resistenza_potenza.png", dpi=220)
