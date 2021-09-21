l = []
print(type(l)) # <class 'list'>

numbers = [2, 19, 14, 10, 6] # liste de 5 entiers
print("Premier chiffre:", numbers[0])
# print(numbers[5]) # IndexError: list index out of range
print("Troisième chiffre:", numbers[1+1]) # computed index

print("Dernier chiffre:", numbers[-1]) # index négatif (inversé), "on part de la fin"

numbers[0] = 4 # accès en écriture
print("Premier chiffre:", numbers[0])

index = 0
for n in numbers:
  #print("Le double de :", n, "est", n * 2)
  numbers[index] = n * 2
  index += 1

for n in numbers:
  print(n)

print("-------------------------------")

numbers.append(20)
numbers.append(5)

for n in numbers:
  print(n)

print("-------------------------------")

for n in enumerate(numbers):
  print(n[0], "=>", n[1])

print("-------------------------------")

for index, value in enumerate(numbers): # enumerate renvoie un tuple contenant index et valeur
  print(index, "=>", value)

