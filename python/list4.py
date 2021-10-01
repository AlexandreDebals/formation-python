students = [
  "Afouda Pamela",
  "Castets Pierre",
  "Debals Alexandre",
  "Pelle Pierre-Jean",
  "Saupagna Sébastien"
]

# Objectif: obtenir un mail à partir de la chaîne Nom Prénom
# Exemple: "Afouda Pamela" => pamela.afouda@python.com

'''
student = "Afouda Pamela".lower() # mise en base de casse
spaceIndex = student.find(" ")
lastname = student[:spaceIndex] # nom de famille
firstname = student[spaceIndex + 1:]
email = firstname + "." + lastname + "@python.com"
print(email)
'''

for s in students:
  student = s.lower() # mise en base de casse
  spaceIndex = student.find(" ")
  lastname = student[:spaceIndex] # nom de famille
  firstname = student[spaceIndex + 1:]
  email = firstname + "." + lastname + "@python.com"
  emailNoAccent = email.replace("é", "e")
  print(emailNoAccent)
  # exemple de chaînage de méthodes de str
  #print(s.lower().replace("é","e").replace("-", "_").upper())