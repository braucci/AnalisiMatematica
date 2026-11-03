"""
cap01_triangolare.py — codice del capitolo 1 (07-lineari-modulo).
Eseguire dalla cartella Libro/:  python3 python/cap01_triangolare.py
"""
# Un esperimento numerico non dimostra nulla, ma aiuta a "vedere"
# quando la disuguaglianza è stretta e quando è un'uguaglianza.
import random
random.seed(1)
for _ in range(6):
    x1, x2 = random.uniform(-5, 5), random.uniform(-5, 5)
    sinistra, destra = abs(x1 + x2), abs(x1) + abs(x2)
    segni = "concordi" if x1 * x2 >= 0 else "discordi"
    rel = "=" if abs(sinistra - destra) < 1e-12 else "<"
    print(f"x1={x1:+.2f} x2={x2:+.2f} ({segni}): "
          f"|x1+x2|={sinistra:.2f} {rel} |x1|+|x2|={destra:.2f}")
