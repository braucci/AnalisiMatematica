"""
fig_sierpinski.py — Capitolo 2, figura del triangolo di Tartaglia modulo 2.
Eseguire dalla cartella Libro/:  python3 python/fig_sierpinski.py
Colora i coefficienti binomiali dispari delle prime N righe: compare il
triangolo di Sierpinski.
"""
import numpy as np
import matplotlib.pyplot as plt

N = 128
griglia = np.zeros((N, 2 * N - 1))        # una riga di Tartaglia per ogni riga
riga = [1]
for n in range(N):
    for k, c in enumerate(riga):
        if c % 2 == 1:                     # coefficiente dispari
            griglia[n, (N - 1 - n) + 2 * k] = 1
    # formula di Stifel, lavorando "modulo 2" per non far crescere i numeri
    riga = [1] + [(riga[k - 1] + riga[k]) % 2 for k in range(1, len(riga))] + [1]

fig, ax = plt.subplots(figsize=(7, 3.6))
ax.imshow(griglia, cmap=plt.matplotlib.colors.ListedColormap(["white", "#1F4E79"]),
          interpolation="nearest", aspect="auto")
ax.set_axis_off()
fig.tight_layout(pad=0.1)
fig.savefig("figure/sierpinski.png", dpi=220)
