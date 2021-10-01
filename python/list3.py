postCodes = [
  67200, 75012, 68520, 15000, 75020,
  67200, 75012, 68520, 15000, 75020,
  67275, 75013, 75990, 15000, 75820
]

# print(len((postCodes))) affiche la longueur de la liste => 10

# code = "75020"
# if code[:2] == "75":
#   print("Paris")

# Combien de codes parisiens ?

numParis = 0
for code in postCodes:
  if code >= 75000 and code < 76000:
    numParis += 1

print("Nombre de codes postaux parisiens: ", numParis, "/", len(postCodes))


