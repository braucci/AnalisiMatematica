"""
fig_curva_hilbert.py — Capitolo 4, le prime iterate della curva di Hilbert.
Eseguire dalla cartella Libro/:  python3 python/fig_curva_hilbert.py
"""
import numpy as np
import matplotlib.pyplot as plt


def hilbert(n):
    """Centri dei 4^n quadratini di lato 2^-n, nell'ordine della
    n-esima iterata della curva di Hilbert (inizio in basso a
    sinistra, fine in basso a destra)."""
    N = 2**n
    punti = []
    for d in range(N * N):
        x = y = 0
        t, s = d, 1
        while s < N:
            rx = 1 & (t // 2)
            ry = 1 & (t ^ rx)
            if ry == 0:                  # rotazione del quadrante
                if rx == 1:
                    x, y = s - 1 - x, s - 1 - y
                x, y = y, x
            x += s * rx
            y += s * ry
            t //= 4
            s *= 2
        punti.append(((x + 0.5) / N, (y + 0.5) / N))
    return np.array(punti)


livelli = (1, 2, 3, 4)
fig, assi = plt.subplots(1, 4, figsize=(7, 2.05))
for ax, n in zip(assi, livelli):
    P = hilbert(n)
    N = 2**n
    for k in range(1, N):                # griglia dei quadratini
        ax.plot([k / N, k / N], [0, 1], color="#C9D7E8", lw=0.6)
        ax.plot([0, 1], [k / N, k / N], color="#C9D7E8", lw=0.6)
    ax.plot([0, 1, 1, 0, 0], [0, 0, 1, 1, 0], color="#5A5A5A", lw=0.8)
    ax.plot(P[:, 0], P[:, 1], color="#1F4E79", lw=1.6 if n < 4 else 1.1)
    ax.plot(*P[0], "o", color="#B4662F", ms=3.5)
    ax.plot(*P[-1], "o", color="#B4662F", ms=3.5)
    ax.set_title(rf"$n={n}$", fontsize=10)
    ax.set_xlim(-0.03, 1.03)
    ax.set_ylim(-0.03, 1.03)
    ax.set_aspect("equal")
    ax.axis("off")
fig.tight_layout(w_pad=1.2)
fig.savefig("figure/curva_hilbert.png", dpi=220, bbox_inches="tight",
            pad_inches=0.04)
