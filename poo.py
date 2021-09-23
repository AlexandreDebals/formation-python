# POO: Programmation Orientée Objet

class Student:
  # attributs/propriétés/caractéristiques
  # visibilité publique par défaut
  firstname = "xxx"
  lastname = "yyy"
  email = "test@test.tt"
  member = True

  # méthodes (fonction définie à l'intérieur d'une classe)
  def getFirstName(self):
    return self.firstname
  
  def getLastName(self):
    return self.lastname

  def getFullName(self):
    return self.firstname + " " + self.lastname

  def getInitials(self):
    return (self.firstname[:1] + self.lastname[:1]).upper()

  # méthodes d'accès en écriture sur les propriétés ciblées (setters)
  def setFirstName(self, firstname):
    self.firstname = firstname

  def setLastName(self, lastname):
    self.lastname = lastname

  def remove(self):
    self.member = False




student1 = Student() # Instancie la classe Student
student2 = Student()
student3 = Student()

student1.setFirstName("Roberto")
student1.setLastName("Baggio")

student2.setFirstName("Alessandro")
student2.setLastName("Nesta")

print(student1.firstname) # accès direct à la propriété firstname
print(student1.getFirstName())  # accès via l'exécution d'une méthode

print(student2.getFullName())
print(student2.getInitials())

if student2.member:
  print(student2.getFullName(), "est membre de l'établissement")

student1.remove()

if student1.member:
  print(student1.getFullName(), "est membre de l'établissement")
else:
  print(student1.getFullName(), "n'est plus membre de l'établissement")

