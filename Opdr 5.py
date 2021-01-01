import random
def getal():
    i = 0
    dictionary = {}
    while i < 100:
        nummer = random.randint(1, 10)
        if nummer not in dictionary:
            dictionary[nummer] = 1
        else:
            dictionary[nummer] += 1
        i += 1
    print(dictionary)

def main():
    getal()

main()