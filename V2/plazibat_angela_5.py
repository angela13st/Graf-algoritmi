def najveci_broj(lista):
    najveci=None
    for el in lista:
        if isinstance(el, (int, float)):
            if najveci is None or el > najveci:
                najveci=el
    return najveci

def najveci_broj_rekurzivno(lista):
    if not lista:
        return None
    if isinstance(lista[0], (int, float)):
        ostatak_max = najveci_broj_rekurzivno(lista[1:])
        if ostatak_max is None or lista[0] > ostatak_max:
            return lista[0]
        else:
            return ostatak_max
    else:
        return najveci_broj_rekurzivno(lista[1:])

lista = [7, 18, 3, 'a', True, (2, 3)]
rezultat = najveci_broj(lista)
rezultat_rekurzivno = najveci_broj_rekurzivno(lista)
print(rezultat) 
print(rezultat_rekurzivno) 