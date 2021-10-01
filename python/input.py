n = input("Tape un nombre entier: ")

# print(type(n)) => toute valeur saisie via la fn input est de type str

square = int(n) * int(n)
print("Le carré de", n, "vaut", square, sep=" ") # espace séparateur de chaîne par défaut

print("Le carré de %s vaut %d" % (n, square))