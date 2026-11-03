"""
cap02_combinatoria.py — codice del capitolo 2 (04-combinatoria).
Eseguire dalla cartella Libro/:  python3 python/cap02_combinatoria.py
"""
import itertools, math

A = ["a1", "a2", "a3"]
disp = list(itertools.permutations(A, 2))   # disposizioni 2 su 3
comb = list(itertools.combinations(A, 2))   # combinazioni 2 su 3
print(len(disp), *(f"({x},{y})" for x, y in disp))
print(len(comb), *(f"{{{x},{y}}}" for x, y in comb))

# Le formule chiuse sono già pronte nella libreria standard
print(math.perm(8, 3), math.comb(8, 3), math.factorial(5))
print(math.comb(90, 6))                     # SuperEnalotto

# Verifica di D(n,k) = C(n,k) * k! per tutti i casi con n <= 10
print(all(math.perm(n, k) == math.comb(n, k) * math.factorial(k)
          for n in range(1, 11) for k in range(0, n + 1)))
