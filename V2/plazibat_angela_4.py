import random

pravila = {
    'kamen': 'škare',
    'škare': 'papir',
    'papir': 'kamen'
}

bodovi_igrac=0
bodovi_racunalo=0
while True: 
    print("Odaberite potez (kamen, škare, papir) ili kraj za izlaz: ")
    odabir_igraca = input().lower()
    if(odabir_igraca=='kraj'):
        break
        
    if odabir_igraca not in pravila:
        print("Pogrešan unos. Molimo unesite 'kamen', 'škare' ili 'papir'.")
        continue
        
            
    odabir_racunala = random.choice(list(pravila.keys()))
    
    #print("Korisnik")
    #print(odabir_igraca)
    
    #print("Racunalo")
    #print(odabir_racunala)
    
    if(odabir_igraca in pravila):
        if odabir_igraca == odabir_racunala:
            print("Neriješeno! Bez bodova.") 
        elif pravila[odabir_igraca] == odabir_racunala:
            print("Igrač pobjeđuje u ovoj rundi!")
            bodovi_igrac+=1
        else:
            print("Računalo pobjeđuje u ovoj rundi.")
            bodovi_racunalo+=1
