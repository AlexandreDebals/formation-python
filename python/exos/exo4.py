'''
*** Exo 4: somme de saisies ***
Créer un programme demandant à l'utilisateur se saisir
un chiffre. Tant que l'utilisateur ne saisit pas la valeur "0",
on lui redemande la saisie d'un chiffre.
En sortie de boucle, on affichera la somme des valeurs saisies ainsi qu'un
récapitulatif des valeurs saisies
Exemples de valeurs saisies par l'utilisateur:
15
2
3
0
=> Somme des valeurs saisies: 20 (15,2,3)
'''
print("*** EXO 4: somme de saisies ***")

def sumNumbers(numbers):
  s = 0 # somme
  for n in numbers:
    s += n
  return s

values = []  # liste pour mémorisation des saisies

while True:
  userInput = int(input("Saisir un chiffre (0 pour quitter le programme): "))
  if userInput == 0:
    break # sortie de boucle immédiate
  else:
    values.append(userInput) # ajout de la valeur saisie dans la liste

#valuesFormatted = str(values).replace("[", "(").replace("]",")")
valuesFormatted = "(valeurs saisies: " + str(values).strip("[]") + ")"

print("Somme des valeurs saisies: ", sumNumbers(values), valuesFormatted)