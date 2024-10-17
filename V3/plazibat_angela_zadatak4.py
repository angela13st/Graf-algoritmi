def procitaj_i_spremi_datoteku_u_rjecnik(datoteka):
    rjecnik = {}
    with open(datoteka, 'r') as file:
        for line in file:
            parts = line.strip().split()
            if len(parts) == 2:
                kljuc, vrijednost = map(int, parts)
                if kljuc not in rjecnik:
                    rjecnik[kljuc] = [vrijednost]
                else:
                    rjecnik[kljuc].append(vrijednost)
    return rjecnik


datoteka = 'podatci.txt'
rezultat = procitaj_i_spremi_datoteku_u_rjecnik(datoteka)
print(rezultat)
