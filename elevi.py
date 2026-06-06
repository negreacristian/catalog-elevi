elevi = [
    {"nume": "Ana", "nota": 9},
    {"nume": "Mihai", "nota": 7},
    {"nume": "Elena", "nota": 8},
    {"nume": "Andrei", "nota": 6},
]

def salveaza_in_fisier():
    with open("rezultate.txt", "w") as f:
        for e in elevi:
            f.write(f"{e['nume']}: {e['nota']}\n")
    print("Salvat in rezultate.txt")

def incarca_din_fisier():
    with open("rezultate.txt", "r") as f:
        continut = f.read()
    print("Date din fisier:\n" + continut)

def afiseaza_elevi():
    print("=== Lista elevi ===")
    for e in elevi:
        print(f"  {e['nume']}: {e['nota']}")

