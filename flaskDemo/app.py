from flask import Flask, render_template

app = Flask(__name__) # instanciation de la classe Flask

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

@app.route("/student/note/")
def studentNote():
  # route retournant la note obtenue par l'étudiant dont le nom/id sera fournie dans l'url
  return ""




app.run(host="0.0.0.0", port=8082)