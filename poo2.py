class Email:
  # corps du message
  _body = "" # simple underscore => protected (accessible depuis l'extérieur, héritée)

  # destinataire
  __dst = "" # double underscore => private (inacessible depuis l'extérieur)

  # méthode constructeur: s'exécute automatiquement à l'instanciation
  def __init__(self, body, dst):
    #print("Constructeur exécuté !")
    self._body = body
    self.__dst = dst


  def getBody(self):
    return self._body

  def getDst(self):
    return self.__dst

  def setBody(self, body):
    self._body = body

  def setDst(self, dst):
    self.__dst = dst


email1 = Email("Ciao", "toto@nada.es") # instanciation

#email1.setBody("Bonjour, ...")
# print(email1.body)
print(f"Corps du message: {email1.getBody()}")


#email1.dst = "destinataire@blabla.fr"
#print(email1.dst)
#email1.setDst("destinataire@blabla.fr")
print(f"Destinataire du message: {email1.getDst()}")
