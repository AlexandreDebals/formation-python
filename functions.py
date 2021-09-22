from tools import separator

# une fonction est une unité code contenant une ou plusieurs
# instructions pouvant être appelée autant de fois que souhaité
# micro-organisme d'entrée/sortie

# def separator(character, times = 50):
#   row = ""
#   for n in range(times):
#     row += character
#   print(row)

separator("*", 30)
# separator("-", 40)
# separator("_")
# separator('>')

def hello():
  #print("Ciao tutti !")
  return "Ciao tutti"

result = hello()
print(result)

def square(n):
  return n * n

#print(square(5))

numbers = [6,4,40,10,8,15]
for n in numbers:
  if n <= 10:
    print(square(n))
