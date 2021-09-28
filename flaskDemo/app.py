from flask import Flask, render_template, Response, request
import json
# make_response

app = Flask(__name__) # instanciation de la classe Flask

# Simulacre de base de données à remplacer ultérieurement par une vraie DB
students = [
  {"id": 1, "name": "Aude", "note": 15},
  {"id": 2, "name": "Jocelyn", "note": 19.5},
  {"id": 3, "name": "Alyssia", "note": 17}
]


@app.route("/")
def home():
  return "Page d'accueil"

@app.route("/login")
def login():
  content = '''
  <!DOCTYPE html>
  <html>
    <head>
      <title>Login</title>
    </head>
    <body>
      <h1>Identification</h1>
    </body>
  </html>
  '''
  return content

@app.route("/page")
def page():
  with open("page.html", "r") as f:
    content = f.read()
    return content

@app.route("/student")
def student():
  studentData = {"name": "Aude", "note": 17}
  return render_template("student.html", s=studentData)

@app.route("/student/<id>/note")
def studentNote(id):
  # route retournant la note obtenue par l'étudiant dont le nom/id sera fournie dans l'url
  
  # l'étudiant existe-t-il en base de données ?
  searchedStudent = None

  for s in students:
    if s["id"] == int(id):
      searchedStudent = s
  
  if searchedStudent == None:
    response = Response(response="Etudiant non trouvé", status=404)
    return response
  else:
    return render_template("student.html", s=searchedStudent)

@app.route("/students")
def studentList():
  return json.dumps(students)

# correction de l'exo9
@app.route("/square/<number>")
def square(number):
  try:
    n = int(number)
  except:
    return "Le calcul du carré de %s est impossible" % number
    
  return "Le carré de %d est: %d" % (n, n*n)

@app.route("/square")
def squareForm():
  if len(request.args) == 0: # pas de QueryString
    return render_template("squareForm.html")
  else: # QueryString présente, contient des paramères
    number = request.args["number"] # accès au paramètre number de la QueryString
    try:
      n = int(number)
    except:
      return "Le calcul du carré de %s est impossible" % number
    
    return "Le carré de %d est: %d" % (n, n*n)
  
  


app.run(host="0.0.0.0", port=8082)