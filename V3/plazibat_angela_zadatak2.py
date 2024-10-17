from plazibat_angela_zadatak1 import procitaj_matricu

def suma_redaka(matrica):
    suma_redaka_lista = []
    for red in matrica:
        suma_redaka = sum(red)
        suma_redaka_lista.append(suma_redaka)
    return suma_redaka_lista

matrica_datoteka = 'matrica.txt'
matrica = procitaj_matricu(matrica_datoteka)

rezultat = suma_redaka(matrica)
print(rezultat)