elevi = [
    {"nume": "Ana", "nota": 9},
    {"nume": "Mihai", "nota": 7},
    {"nume": "Elena", "nota": 8},
    {"nume": "Andrei", "nota": 6},
    {"nume": "Andrei", "nota": 10},
    {"nume": "Andrei", "nota": 5},
    {"nume": "Andrei", "nota": 8},
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



def calculeaza_medie():
    medie = 0
    total_elevi = 0

    for i in elevi:
        note = i['nota']
        medie += note
        total_elevi += 1
    
    medie /= total_elevi
    print(medie)

def cel_mai_bun():
    max_elev = None
    Nota_Mare = 0
    for i in elevi:
        if i['nota'] > Nota_Mare:
            Nota_Mare = i["nota"]
            max_elev = i["nume"]
    print(f"Elevul {max_elev}, are cea mai mare nota din clasa, nota {Nota_Mare}")

def sortare_elevi():
    lista = elevi[:]
    print(lista)
    for i in range(0, len(lista)):
        for j in range(i+1, len(lista)):
            if lista[j]['nota'] > lista[i]['nota']:
                lista[i], lista[j] = lista[j], lista[i]
    print(lista)



