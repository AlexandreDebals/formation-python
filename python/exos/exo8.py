'''
*** EXO 8: Heath Check ***
Créer un programme qui, à partir du fichier websites.txt,
vérifie que chacun des sites listées répond à la requête.

Les sites (serveurs) seront interrogés toutes les n secondes.

la périodicité (n) sera fournie en entrée par l'utilisateur

On produira en sortie un fichier de log "health.log" qui contiendra:
- la date de la requête
- l'url interrogée
- le status code obtenu ou une indication d'erreur en cas de non réponse

Il faudra éviter d'écraser le fichier de log
'''
print("*** EXO 8: Health Check ***")

# votre code ici
import time, datetime
import requests
import sys

startTime = time.time()
logFilePath = "health.log"

#sleepTime = int(input("Entrez le temps en seconde entre deux requêtes: "))
#maxTime = 30 # temps d'exécution maximale du script

# ToDo: vérifier que les arguments on été fournis à la commande
# et qu'ils sont "acceptables" (convertibles en entier)
sleepTime = int(sys.argv[1])
maxTime = int(sys.argv[2])

with open("websites.txt", "r") as sites:
    websites = sites.read().splitlines()

while True:
    logFile = open(logFilePath, "a")
    for w in websites:
        newLogLine = ""
        newLogLine += str(datetime.datetime.now()) + " " + w + " "
        #print(newLogLine)
        try:
            response = requests.get(w)
            newLogLine += str(response.status_code)
        except:
            newLogLine += "error when requesting the website"
        logFile.write(newLogLine + "\n")
    logFile.close()
    time.sleep(sleepTime)
    if time.time() - startTime > maxTime:
        break