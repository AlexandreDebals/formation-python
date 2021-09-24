import platform, os
import tools
import mypackage.subpackage.subdemo as subd
from colorama import Fore, Style

# print(platform.processor())
# print(platform.system())
# print(os.name)
# print(os.getcwd())

#for x in range(5):
  #os.mkdir('tmp_' + str(x+1))
  #os.rmdir('tmp_' + str(x+1))

# alphabetMin = []
# for x in range(97, 123): # itération sur un range ASCII https://www.asciitable.com/
#   alphabetMin.append(chr(x))

# équivalent
# alphabetMin = [ 'a' for i in range (97,123) ]
# print(alphabetMin)

#students = ["Sébastien", "Pamela", "Aude"]
# lenNames = [ len(s) for s in students ]

# countries = ["allemagne", "italie", "france"]
# countriesBis = [ c[:2].upper() for c in countries ]

# tools.randSeparator()
# tools.example()

#subd.subdemoprint() # exécution d'une fonction placée dans un sous-package importé et aliasé

# utilisation du module colorama afin
# d'afficher le texte en vert
# RESET_ALL permet de retrouver la couleur par défaut

#print(Fore.GREEN + 'Bravo !' + Style.RESET_ALL)
#print('Tu es le meilleur !')

s = "n\n\n<!DOnCTYPE n"

s2 = s.replace("n", "x").replace("\n", "---")
print(s2)