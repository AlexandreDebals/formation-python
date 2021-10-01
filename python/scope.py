message = "J'aime Python" # variable de portée (scope) globale

def f1():
  privateMessage = "Secret" # variable de portée locale, inacessible depuis l'extérieur de fonction
  #print(message)
  #f2()
  message = "J'adore Python" # création d'une variable locale
  print(message) # accès à la variable locale, prioritaire par rapport à la variable globale de même nom
  
def f2():
  print(message)
  #print(privateMessage) # interdit !

f1()
f2()



# print(privateMessage) # interdit !