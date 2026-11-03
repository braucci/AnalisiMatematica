"""
fig_radici_unita.py — Capitolo 2, radici n-esime dell'unità per n = 3..8.
Eseguire dalla cartella Libro/:  python3 python/fig_radici_unita.py
"""
import cmath, math
import matplotlib.pyplot as plt

fig, assi = plt.subplots(1, 6, figsize=(10, 2.15))
for ax, n in zip(assi, range(3, 9)):
    # formula delle radici: modulo 1, argomenti 2k*pi/n
    radici = [cmath.exp(2j * math.pi * k / n) for k in range(n)]
    xs = [w.real for w in radici] + [radici[0].real]
    ys = [w.imag for w in radici] + [radici[0].imag]
    t = [2 * math.pi * s / 200 for s in range(201)]
    ax.plot([math.cos(u) for u in t], [math.sin(u) for u in t], color="#5A5A5A", lw=0.6, alpha=0.6)
    ax.fill(xs, ys, color="#C9D7E8", alpha=0.6)
    ax.plot(xs, ys, color="#1F4E79", lw=1.2)
    ax.plot(xs[:-1], ys[:-1], "o", color="#B4662F", ms=3.5)
    ax.axhline(0, color="#5A5A5A", lw=0.4)
    ax.axvline(0, color="#5A5A5A", lw=0.4)
    ax.set_title(f"$z^{{{n}}}=1$", fontsize=10)
    ax.set_aspect("equal"); ax.set_xlim(-1.25, 1.25); ax.set_ylim(-1.25, 1.25)
    ax.set_xticks([]); ax.set_yticks([])
    for s in ax.spines.values():
        s.set_visible(False)
fig.tight_layout(pad=0.6)
fig.savefig("figure/radici_unita.png", dpi=220)
