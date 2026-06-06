elevi = [
    {"nume": "Ana", "nota": 9},
    {"nume": "Mihai", "nota": 7},
    {"nume": "Elena", "nota": 8},
    {"nume": "Andrei", "nota": 6},
]

def afiseaza_elevi():
    print("=== Lista elevi ===")
    for e in elevi:
        print(f"  {e['nume']}: {e['nota']}")
