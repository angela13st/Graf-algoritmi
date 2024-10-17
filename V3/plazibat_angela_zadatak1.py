def procitaj_matricu(datoteka):
    try:
        with open(datoteka, 'r') as file:
            matrica = [list(map(int, line.strip().split())) for line in file.readlines()]
            return matrica
    except FileNotFoundError:
        print(f"Datoteka '{datoteka}' nije pronađena.")
        return None
    except Exception as e:
        print(f"Došlo je do pogreške: {e}")
        return None

def zbroj_dijagonala(matrica):
    if not all(len(row) == len(matrica) for row in matrica):
        return 0, 0

    n = len(matrica)
    zbroj_glavne_dijagonale = 0
    zbroj_sporedne_dijagonale = 0

    for i in range(n):
        for j in range(n):
            if i < j:
                zbroj_glavne_dijagonale += matrica[i][j]
            if i + j < n - 1:
                zbroj_sporedne_dijagonale += matrica[i][j]

    return zbroj_glavne_dijagonale, zbroj_sporedne_dijagonale

if __name__ == "__main__":
    matrica_datoteka = 'matrica.txt'
    matrica = procitaj_matricu(matrica_datoteka)
    zbroj_glavne, zbroj_sporedne = zbroj_dijagonala(matrica)
    if zbroj_glavne == 0 and zbroj_sporedne == 0:
        print("Matrica nije kvadratna.")
    else:
        print(f"Zbroj elemenata iznad glavne dijagonale: {zbroj_glavne}")
        print(f"Zbroj elemenata iznad sporedne dijagonale: {zbroj_sporedne}")
