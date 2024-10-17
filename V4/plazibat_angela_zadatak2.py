from plazibat_angela_zadatak1 import read_pajek_file


def broj_vrhova(lista_susjedstava):
    return len(lista_susjedstava)

def broj_bridova(lista_susjedstava):
    brojac_bridova = sum(len(susjedi) for susjedi in lista_susjedstava.values()) // 2
    return brojac_bridova

def stupanj_svakog_vrha(lista_susjedstava):
    stupnjevi = {vrh: len(susjedi) for vrh, susjedi in lista_susjedstava.items()}
    return stupnjevi

def vrhovi_s_maksimalnim_stupnjem(lista_susjedstava):
    stupnjevi = stupanj_svakog_vrha(lista_susjedstava)
    maksimalni_stupanj = max(stupnjevi.values())
    vrhovi_maksimalnog_stupnja = [vrh for vrh, stupanj in stupnjevi.items() if stupanj==maksimalni_stupanj]
    return vrhovi_maksimalnog_stupnja


file_path = 'euler.net'
adjacency_list = read_pajek_file(file_path)

print("Broj vrhova:", broj_vrhova(adjacency_list))

print("Broj bridova:", broj_bridova(adjacency_list))

print("Stupnjevi vrhova:", stupanj_svakog_vrha(adjacency_list))

print("Vrhovi s maksimalnim stupnjem:", vrhovi_s_maksimalnim_stupnjem(adjacency_list))
