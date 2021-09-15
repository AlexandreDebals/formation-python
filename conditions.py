isEarthRound = True
message = "2 est strictement supérieur à 1"
condition = 2 > 1 # équivalent condition = True

if isEarthRound == True:
  print("La terre est ronde")

# version courte
if isEarthRound:
  print("La terre est ronde")

if condition:
  print(message)

n = 7
observeFifaRules = True

if n >= 7 and observeFifaRules:
  print("Assez nombreux pour jouer au foot")
else:
  print("Pas assez nombreux pour jouer au foot")

exemple1 = False or True
exemple2 = False and True
exemple3 = not False
print("False or True =>", exemple1)
print("False and True =>", exemple2)
print("not False =>", exemple3)


