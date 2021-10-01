import csv # module csv built-in

cityNameIndex = 8
n = 0

with open("files/cities.csv", "r") as csvFile:
  rows = csv.reader(csvFile, delimiter=",")
  rows2 = [1,5,6]
  for r in rows:
    cityName = r[8].strip().strip("\"")
    if cityName.startswith("San"):
      n += 1

print("Nombre de villes trouvées: %d" % n)