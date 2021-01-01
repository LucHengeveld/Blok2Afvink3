def opdr6():
    bestand1 = open("bestand1", "r").read()
    bestand2 = open("bestand2", "r").read()

    lijst1 = bestand1.split(" ")
    lijst2 = bestand2.split(" ")

    set1 = set(())
    set2 = set(())

    for i in range(len(lijst1)):
        set1.add(lijst1[i])
    for j in range(len(lijst2)):
        set2.add(lijst2[j])

    print("Unieke woorden:", set1.symmetric_difference(set2))
    print("Intersection:", set1.intersection(set2))
    print("First file only:", set1.difference(set2))
    print("Second file only:", set2.difference(set1))
    print("Either first or second:", set1.difference(set2),
          set2.difference(set1))


def main():
    opdr6()


main()
