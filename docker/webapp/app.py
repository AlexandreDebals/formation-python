from flask import Flask, render_template
import mysql.connector # import du client mysql
import json, os

# accès aux variables d'environnement
# permet plus de flexibilité concernant la connexion à la DB
MYSQL_HOST = os.environ.get("MYSQL_HOST")
MYSQL_PORT = os.environ.get("MYSQL_PORT")

# connection au serveur mysql
db = mysql.connector.connect(
  #host="sql1",
  #port=3306,
  host=MYSQL_HOST,
  port=MYSQL_PORT,
  user="root",
  password="root",
  database="webapp"
)

app = Flask(__name__)

@app.route("/")
def home():
  return "ok"

@app.route("/student")
def student():
  cursor = db.cursor()
  cursor.execute("select * from student")
  students = cursor.fetchall() # convertit le retour/resultat sql en structure Python
  #print(students)
  #return json.dumps(students) # renvoie des données au format JSON
  return render_template("student.html", students=students)

@app.route("/student/<id>")
def studentDetail(id):
  cursor = db.cursor()
  sql = "select firstname, note from student where id = %s"
  params = (id, )
  cursor.execute(sql, params)
  firstname, note = cursor.fetchall()[0]
  resp = f"{firstname} a obtenu la note de: {note}/20"
  return resp

@app.route("/exo2")
def exo2():
  # on recherche les étudiants ayant obtenu au moins 10/20
  cursor = db.cursor()
  cursor.execute("select * from student where note >= 10")
  students = cursor.fetchall()
  return render_template("student.html", students=students)

# démarrage du serveur
app.run(host="0.0.0.0", port=8080)