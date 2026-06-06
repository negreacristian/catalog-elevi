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



def media_pe_clasa():
    medie = 0
    total_elevi = 0

    for i in elevi:
        note = i['nota']
        medie += note
        total_elevi += 1
    
    medie /= total_elevi
    print(medie)

