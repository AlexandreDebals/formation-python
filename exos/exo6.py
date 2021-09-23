'''
*** Exo 6: Générateur de mot de passe ***
Créer un programme qui génère un mot de passe de longueur variable
en concaténant des caractères de façon aléatoire.
Le mot de passe devra contenir:
- au moins une majuscule
- au moins une minuscule
- au moins une valeur numérique
- au moins un caractère spécial (/;|%, etc.)

La longueur sera donnée par une saisie utilisateur
ex: longueur: 8 => Hn_y9l2%
'''
print("*** EXO 6: Générateur de mot de passe ***")

#import string
from random import shuffle, choice, randint

lowerLetter = string.ascii_lowercase
upperLetter = string.ascii_uppercase
specialCharacters = string.punctuation

passwordLen = int(input("Saisir la longueur du mot de passe souhaité : "))
numCase = 0
password = []
counter = 0

while counter < passwordLen:
  if numCase == 0:
    password.append(choice(lowerLetter))
    numCase += 1
    counter += 1
  elif numCase == 1:
    password.append(choice(upperLetter))
    numCase += 1
    counter += 1
  elif numCase == 2:
    password.append(str(randint(0, 9)))
    numCase += 1
    counter += 1
  elif numCase == 3:
    password.append(choice(specialCharacters))
    numCase += 1
    counter += 1
  else:
    numCase = 0

shuffle(password)
print("Le mot de passe est: %s" % "".join(password))






