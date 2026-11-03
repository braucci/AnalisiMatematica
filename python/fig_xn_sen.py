"""
fig_xn_sen.py — Capitolo 5, le funzioni x sen(1/x), x^2 sen(1/x) e la derivata della seconda.
Eseguire dalla cartella Libro/:  python3 python/fig_xn_sen.py
"""
import numpy as np
import matplotlib.pyplot as plt

blu, rame, grigio = "#1F4E79", "#B4662F", "#5A5A5A"
t = np.linspace(1 / 0.25, 3000, 600000)
rami = (-1 / t, 1 / t[::-1])
z = np.linspace(-0.25, 0.25, 3)
fig, axs = plt.subplots(1, 3, figsize=(8.6, 2.9))
for x in rami:
    axs[0].plot(x, x * np.sin(1 / x), color=blu, lw=0.5)
    axs[1].plot(x, x**2 * np.sin(1 / x), color=blu, lw=0.5)
    axs[2].plot(x, 2 * x * np.sin(1 / x) - np.cos(1 / x), color=rame, lw=0.35)
axs[0].plot(z, np.abs(z), "--", color=grigio, lw=0.9); axs[0].plot(z, -np.abs(z), "--", color=grigio, lw=0.9)
zz = np.linspace(-0.25, 0.25, 200)
axs[1].plot(zz, zz**2, "--", color=grigio, lw=0.9); axs[1].plot(zz, -zz**2, "--", color=grigio, lw=0.9)
axs[0].set_title(r"$f_1(x)=x\,\mathrm{sen}\,(1/x)$", fontsize=10)
axs[1].set_title(r"$f_2(x)=x^2\,\mathrm{sen}\,(1/x)$", fontsize=10)
axs[2].set_title(r"$f_2'(x)$ per $x\neq0$", fontsize=10)
axs[0].set_ylim(-0.27, 0.27); axs[1].set_ylim(-0.07, 0.07); axs[2].set_ylim(-1.6, 1.6)
axs[2].plot([0], [0], "o", color=blu, ms=4, zorder=3)
for ax in axs:
    ax.set_xlim(-0.25, 0.25)
    ax.axhline(0, color="black", lw=0.6); ax.axvline(0, color="black", lw=0.6)
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
    ax.tick_params(labelsize=7.5)
fig.tight_layout()
fig.savefig("figure/xn_sen.png", dpi=220)
