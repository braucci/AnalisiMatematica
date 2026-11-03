"""
cap08_corda_media.py — codice del capitolo 8 (04-media).
Eseguire dalla cartella Libro/:  python3 python/cap08_corda_media.py
"""
b, cr, ct = 11.0, 1.6, 1.1           # apertura e corde [m]
s = b / 2                            # semiapertura

def c(y):
    """Corda della semiala trapezia alla stazione y."""
    return cr - (cr - ct) * y / s

def media(g, a, b, n=1000):
    """Media integrale di g con una somma ai punti medi."""
    h = (b - a) / n
    return sum(g(a + (k + 0.5) * h) for k in range(n)) / n

c_med = media(c, 0, s)               # corda media geometrica
S = 2 * s * c_med                    # superficie alare
c_ma = media(lambda y: c(y)**2, 0, s) / c_med
ex = 2 / 3 * (cr**2 + cr * ct + ct**2) / (cr + ct)
print(f"S = {S:.4f} m^2   (esatto {(cr + ct) * s:.4f})")
print(f"corda media  = {c_med:.4f} m   AR = {b**2 / S:.3f}")
print(f"corda m.a.   = {c_ma:.4f} m   (esatto {ex:.4f})")
y0 = (cr - c_med) * s / (cr - ct)    # c(y0) = corda media
y_ma = (cr - c_ma) * s / (cr - ct)   # c(y_ma) = corda m.a.
print(f"stazioni: y0 = {y0:.3f} m,  y_ma = {y_ma:.3f} m")
