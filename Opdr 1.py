def moons():
    radius = {"Io": 1821.6, "Europa": 1560.8, "Ganymede": 2634.1, "Callisto": 2410.3}
    surface = {"Io": 1.796, "Europa": 1.314, "Ganymede": 1.428, "Callisto": 1.235}
    orbital = {"Io": 1.769, "Europa": 3.551, "Ganymede": 7.154, "Callisto": 16.689}

    maan = input("Geef hier een maan van Jupiter: ")

    print("Radius:", radius[maan])
    print("Surface:", surface[maan])
    print("Orbital:", orbital[maan])

def main():
    moons()

main()