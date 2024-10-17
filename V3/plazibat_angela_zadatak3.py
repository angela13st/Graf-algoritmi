from plazibat_angela_zadatak1 import procitaj_matricu

def provjeri_stupce(matrica):
    if not matrica:
        return False  

    broj_redaka = len(matrica)
    broj_stupaca = len(matrica[0])

    for stupac in range(broj_stupaca):
        broj_jedinica = 0
        for redak in range(broj_redaka):
            if matrica[redak][stupac] == 1:
                broj_jedinica += 1
            elif matrica[redak][stupac] != 0:
                return False  
        if broj_jedinica != 2:
            return False  
        
    return True  

matrica1 = [
    [1, 1, 0],
    [1, 1, 1],
    [0, 0, 1]
]

matrica_datoteka = 'matrica.txt'
matrica = procitaj_matricu(matrica_datoteka)
print(provjeri_stupce(matrica))
print(provjeri_stupce(matrica1))