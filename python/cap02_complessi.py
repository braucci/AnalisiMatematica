"""
cap02_complessi.py — codice del capitolo 2 (06-complessi).
Eseguire dalla cartella Libro/:  python3 python/cap02_complessi.py
"""
import cmath, math

z = 3 + 2j          # in Python l'unità immaginaria si scrive j
w = 1 - 1j
print(z / w)                       # quoziente: (0.5+2.5j)
print(abs(z), z.conjugate())       # modulo e coniugato
print(cmath.polar(1j))             # (modulo, argomento) di i

# Radici n-esime con la formula del teorema
def radici(z, n):
    rho, theta = cmath.polar(z)
    r = rho ** (1 / n)
    return [cmath.rect(r, (theta + 2 * k * math.pi) / n)
            for k in range(n)]

for w_k in radici(1j, 2):
    print(f"{w_k:.6f}   (w_k)^2 = {w_k**2:.6f}")

# Dagli assi vento agli assi corda (esempio): F_c = F_v * e^(i alfa)
L, D, alfa = 1000.0, 50.0, math.radians(5)
Fc = complex(D, L) * cmath.exp(1j * alfa)
print(f"A = {Fc.real:.1f} N,  N = {Fc.imag:.1f} N")

# Il calcolo di Bombelli: (2 + i)^3 = 2 + 11i, cioè 2 + sqrt(-121)
print((2 + 1j) ** 3)
