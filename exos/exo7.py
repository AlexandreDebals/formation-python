'''
*** EXO 7: CSV De Niro ***
Créer un programme qui, à partir du fichier deniro.csv,
produira en sortie un fichier deniroReport.txt" 
affichant les informations suivantes:

Nom du film le mieux noté
Nombre de films entre 2000 et 2010

'''
print("*** EXO 7: CSV De Niro ***")

# votre code ici
import csv

with open("deniro.csv", "r") as csvFile :
    rows = csv.reader(csvFile, delimiter=",")
    next(rows, None) # ignore la ligne d'entêtes
    bestScore = 0
    numMovies = 0
    bestMovieTitle = ""
    for r in rows :
      year = int(r[0].strip())
      score = int(r[1].strip())
      title = r[2].strip().strip("\"")
      if score > bestScore:
        bestScore = score
        bestMovieTitle = title
      if year > 1999 and year < 2011:
        numMovies += 1

with open("deniroReport.txt", "w") as txtFile :
  txtFile.write(f"Le titre du film ayant obtenu le meilleur score est {bestMovieTitle}.\nEntre 2000 et 2010 Deniro a joué dans {numMovies} films")
