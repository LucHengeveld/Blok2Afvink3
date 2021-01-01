import pickle
def opdr8():
    try:
        dictionary = pickle.load(open("save.opdr8", "rb"))

    except:
        dictionary = {}

    ant1 = input("Wil je de lijst printen? ja of nee? ")
    if ant1 == "ja":
        print(dictionary)

    ant2 = input("Wil je wat toevoegen? ja of nee? ")
    if ant2 == "ja":
        groente = input("Wat wil je toevoegen? ")
        prijs1 = input("Wat is de bijbehorende prijs? ")
        dictionary[groente] = prijs1

    ant3 = input("Wil je een prijs aanpassen? ja of nee? ")
    if ant3 == "ja":
        aanpassen = input("Wat wil je aanpassen? ")
        prijs2 = input("Wat is de nieuwe prijs? ")
        dictionary[aanpassen] = prijs2

    ant4 = input("Wil je er een verwijderen? ja of nee? ")
    if ant4 == "ja":
        verwijderen = input("Wat wil je verwijderen? ")
        del dictionary[verwijderen]

    print(dictionary)

    pickle.dump(dictionary, open("save.opdr8", "wb"))

def main():
    opdr8()

main()