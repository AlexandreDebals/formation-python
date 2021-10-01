f = open("files/cities.csv", "r")
content = f.read() # lecture du fichier et stockage de son contenu
f.close()

# content2 = f.read() # impossible, le fichier a été fermé

rows = content.splitlines()
cityNameIndex = 8
n = 0 # compteur du nombre villes correspondant aux critères de recherche

for r in rows:
  cols = r.split(",") # virgule, comme séparateur de colonnes
  cityName = cols[cityNameIndex].strip().strip("\"") # enlève les espaces en début/fin de chaîne, enlève les guillements début/fin de chaîne
  #print(cityName, "=>", len(cityName))
  if cityName.startswith("San"):
    n += 1

print("Nombre de villes trouvées: %d" % n)

# r = "toto-tata-titi".split("-")
# print(r)

# s = " \"Yakima\"".strip().strip('"')
# print(len(s))

  



