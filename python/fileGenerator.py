'''
f = open("blabla.txt", "r") # r => lecture
print(f.read())
f.close()

f = open("test.txt", "x") # x, a, w => écriture
f.write("Simple fichier")
f.close()
'''
from random import randint
import os

def getRandomValue(l):
  randIndex = randint(0, len(l) - 1)
  return l[randIndex]

numFiles = 10 # nombre de fichiers à générer
fileNames = ["script", "demo", "example", "test", "new"]
extensions = ["txt", "log", "json", "js", "exe"]
targetDir = "files/"

# for x in range(numFiles):
#   filename = targetDir + getRandomValue(fileNames) + "." + getRandomValue(extensions)
#   f = open(filename, "w")
#   f.close()
#   print("Création du fichier '%s'" % filename)

# avant de créer les fichiers, vérifier que le dossier cible existe
dirExists = os.path.isdir(targetDir)
if not dirExists:
  print("Le dossier cible '%s' n'existe pas" % targetDir)
  try:
    os.mkdir(targetDir)
    print("Le dossier cible '%s' a été créé" % targetDir)
  except:
    print("Impossible de créer le dossier cible '%s'" % targetDir)
    exit()
  
# création des fichiers
for x in range(numFiles):
  filename = targetDir + getRandomValue(fileNames) + "." + getRandomValue(extensions)
  print("\nTentative de création du fichier'%s'" % filename)

  try:
    f = open(filename, "x")
    f.close()
    print("=> succès")
  except FileExistsError:
    print("=> le fichier existe déjà")
  except:
    print("=> erreur")


  

