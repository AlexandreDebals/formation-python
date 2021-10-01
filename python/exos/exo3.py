'''
*** Exo 3 ***
Ecrire un script python, qui calculera et affichera le prix TTC de prix HT
Créer et utiliser une fonction qui calculera le prix TTC du prix 
HT qu'on lui fournira en entrée
'''
print("*** EXO 3 ***")

prices = [14,100,30,10,8] # prix HT

def getPriceWithVat(price, vat = 20):
  return round(price * (1 + vat/100), 2) # retour du prix TTC arrondi

for price in prices:
  print(getPriceWithVat(price, 7))
