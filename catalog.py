import json
class Elev:
    def __init__(self, nume, nota):
        self.nume = nume
        self.nota = nota
    def __str__(self):
        return self.nume, self.nota
    def to_dict(self):
        return {'nume': self.nume,'nota': self.nota}

class Catalog:
    def __init__(self, elevi = []):
        self.elevi = elevi

    def adauga(self, elev):
        self.elevi.append(elev)
        
    def __str__(self):
        return self.elevi    

    def afiseaza(self):
        print("=== Lista elevi ===")
        for e in self.elevi:
            print(f"  {e.nume}: {e.nota}")
    
    def medie(self):
        medie = 0
        total_elevi = 0

        for i in self.elevi:
            note = i.nota
            medie += note
            total_elevi += 1
    
        medie /= total_elevi
        print(medie)
    
    def cel_mai_bun(self):
        max_elev = None
        Nota_Mare = 0
        for i in self.elevi:
            if i.nota > Nota_Mare:
                Nota_Mare = i.nota
                max_elev = i.nume
        print(f"Elevul {max_elev}, are cea mai mare nota din clasa, nota {Nota_Mare}")
    
    
    
    def salveaza(self):
        try:
            with open('fisier.txt', 'w') as f:
                for elev in self.elevi:
                    json.dump(elev.to_dict(), f, indent=4)
            print("Salvat in fisier.txt")
        except FileNotFoundError:
            return []

e1 = Elev('Edi', 7)
e2 = Elev('Mihai', 5)

c = Catalog()

c.adauga(e1)
c.adauga(e2)
c.afiseaza()

c.medie()
c.cel_mai_bun()
c.salveaza()