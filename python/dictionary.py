from tools import separator # import de module personnalisé (tools.py)

# Un dictionnaire est une structure clé/valeur
# permettant de modéliser une information/entité
d = {}
#print(type(d)) # <class 'dict'>

student = {
  "firstname": "Chris", 
  "lastname": "Dufour",
  "email": "c.dufour@python.com",
  "age": 99,
  "rates": [8, 12, 17]
}

print(student["firstname"], "a", student.get("age"), "ans")
student["lastname"] = "DUFOUR" # modifie l'attribut lastname
student["rates"].append(15) # ajoute une note à la liste
student["tel"] = "0788996633" # ajoute une nouvelle clé
student.pop("age") # supprime la clé

separator("-")

for x in student:
  # affiche la clé et la valeur associée
  print(x, "=>", student[x])

separator("-")

for v in student.values(): # itére uniquement sur les valeurs du dict
  print(v)

separator("-")

for k in student.keys(): # itére uniquement sur les clés du dict
  print(k)
