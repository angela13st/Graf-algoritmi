from plazibat_angela_zadatak1 import read_pajek_file


def is_eulerian(lista_susjedstava):
    if not is_connected(lista_susjedstava):
        return False

    stupnjevi = {vrh: len(susjedi) for vrh, susjedi in lista_susjedstava.items()}

    if any(stupanj % 2 == 1 for stupanj in stupnjevi.values()):
        return False

    return True

def is_connected(lista_susjedstava):
    posjeceni = set()

    def dfs(vrh):
        posjeceni.add(vrh)
        for susjed in lista_susjedstava[vrh]:
            if susjed not in posjeceni:
                dfs(susjed)

    pocetni_vrh = next(iter(lista_susjedstava))
    dfs(pocetni_vrh)

    return len(posjeceni) == len(lista_susjedstava)

file_path = 'euler.net'
adjacency_list = read_pajek_file(file_path)

if is_eulerian(adjacency_list):
    print("Graf je Eulerov.")
else:
    print("Graf nije Eulerov.")

eulerov_graf = {
    1: [2, 3, 4, 5],
    2: [1, 3, 4, 5],
    3: [1, 2, 4, 5],
    4: [1, 2, 3, 5],
    5: [1, 2, 3, 4]
}

if is_eulerian(eulerov_graf):
    print("Graf je Eulerov.")
else:
    print("Graf nije Eulerov.")
