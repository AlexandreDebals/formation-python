title = "Les Trois Mousquetaires"

# for letter in title:
#   print(letter)

#print(title[0]) # L
# title[0] = 'D' # TypeError les chaînes ne sont pas accesssibles en écriture

word = ""
for letter in title[4:9]:
  word += letter

#print(word)

numOccurences = 0
#searchedLetter = "a"
searchedLetter = input("Lettre à rechercher: ")

for letter in title:
  if letter == searchedLetter:
    numOccurences += 1

print("La lettre: \"%s\" a été trouvée %s fois dans le titre: %s" 
  % (searchedLetter, numOccurences, title))

