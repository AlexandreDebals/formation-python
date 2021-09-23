import platform, os
import tools

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

tools.randSeparator()
tools.example()