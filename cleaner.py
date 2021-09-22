# Ce script supprime les fichiers .txt qu'il trouve
# dans le dossier cible

import os

numRemovedFiles = 0
files = os.listdir("files")

for f in files:
  extension = f[-3:]
  if extension == "txt":
    os.remove("files/" + f)
    numRemovedFiles += 1
    print("Fichier '%s' supprimé" % f)

print("%d fichiers ont été supprimés" % numRemovedFiles)