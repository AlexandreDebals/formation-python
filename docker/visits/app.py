'''
Démonstration de la communication
entre une application Flask et un serveur Redis
'''

from flask import Flask
import redis
import os

REDIS_HOST = os.environ.get("REDIS_HOST")

# instanciation d'un client redis
r = redis.Redis(host=REDIS_HOST, port=6379, db=0)

app = Flask(__name__)

@app.route("/")
def home():
  numVisits = r.get("visits")
  if numVisits == None:
    numVisits = 0
  numVisits = int(numVisits)
  r.set("visits", numVisits + 1)
  return f'*** Nombre de visites: {numVisits} ***\n'

# démarrage du serveur
app.run(host="0.0.0.0", port=8080)