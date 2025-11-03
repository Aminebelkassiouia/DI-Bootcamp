# Exercice 3 : Booléens et comparaisons

print("3 == 3 == 3 ->", 3 == 3 == 3)
print("3 <= 3 < 9 ->", 3 <= 3 < 9)
print("bool(0) ->", bool(0))
print('bool(5 == "5") ->', bool(5 == "5"))
print('bool(4 == 4) == bool("4" == "4") ->', bool(4 == 4) == bool("4" == "4"))
print("bool(bool(None)) ->", bool(bool(None)))

x = (1 == True)
y = (1 == False)
a = True + 4
b = False + 10

print("\nRésultats des variables : x =", x, ", y =", y, ", a =", a, ", b =", b)

# Exercice 4 : Longueur du texte

print("\nExercice 4 : Longueur du texte\n")

texte = (
    "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt "
    "ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco "
    "laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in "
    "voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat "
    "non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
)

print("Longueur du texte :", len(texte))

# Exercice 5 : Phrase la plus longue sans 'A'

record = ""
while True:
    phrase = input("Tape une phrase sans 'A' : ")
    if 'A' in phrase.upper():
        print("Attention, il y a un 'A' !")
        continue
    if len(phrase) > len(record):
        record = phrase
        print("Bravo ! Nouveau record :", len(record), "caractères")
