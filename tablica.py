import random
import webbrowser

def provjeri_znanje():
    # Unos broja pitanja od korisnika
    broj_pitanja = int(input("Unesite broj pitanja za provjeru (do 100): "))
    # u slučaju da je unešen broj pitanja veći od 100
    # broj pitanja se postavlja kao 100 jer tablica množenja
    # ima 100 pitanja
    broj_pitanja = min(broj_pitanja, 100)

    tablica = list(range(1, 11))  # lista brojeva za izbor
    pitanja = []  # Lista za pohranu pitanja
    n_odgovori = []  # Lista za pohranu netočnih odgovora

    # Generiranje nasumičnih pitanja
    while len(pitanja) < broj_pitanja:
        X = random.choice(tablica)
        Y = random.choice(tablica)
        pitanje = f"{X} * {Y} = "
        if (pitanje, X * Y) not in pitanja:
            pitanja.append((pitanje, X * Y))

    # Provjera znanja
    while n_odgovori or pitanja:
        if not pitanja:
            pitanja = n_odgovori.copy()
            n_odgovori = []
            print("**************************************")
            print("Ispitivanje za brojeve koje nisi znao:")

        pitanje, odgovor = pitanja.pop(0)
        korisnikov_odgovor = input(pitanje)
        if int(korisnikov_odgovor) != odgovor:
            n_odgovori.append((pitanje, odgovor))

    print("****************")
    print("***BRAVOOOO*****")
    print("****************")
    # kao nagradu otvara stranicu sa matematičkim igricama ili neki drugi link
    webbrowser.open('https://mathgames.com')
provjeri_znanje()
