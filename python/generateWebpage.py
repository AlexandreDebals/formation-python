template = '''
<!DOCTYPE html>
<html>
  <head>
    <title>[name]</title>
    <meta charset="UTF-8">
  </head>
  <body>
    <h1>[name]</h1>
    <p>Vous avez obtenu la note de: [note] sur 20</p>
  </body>
</html>
'''

students = [
  { "name": "Sébastien", "note": 16 },
  { "name": "Pamela", "note": 19.5 },
  { "name": "Aude", "note": 17 }
]

for s in students:
  filepath = "files/" + s["name"].lower().replace("é", "e") + "_note.html"
  content = template.replace("[name]", s["name"]).replace("[note]", str(s["note"]))
  with open(filepath, "w") as f:
    f.write(content)
  print("Fichier html généré pour l'étudiant %s" % s["name"])