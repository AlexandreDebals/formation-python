# Variables primitives

training = "Initiation au langage Python"
temperature = 15
pi = 3.14
isEarthRound = True

print(type(training)) # <class 'str'>
print(type(temperature)) # <class 'int'>
print(type(pi)) # <class 'float'>
print(type(isEarthRound)) # <class 'bool'>

# Opérations sur variables
print(temperature + 10) # addition
print(training + " 10") # concaténation
print(pi + 10)
print(isEarthRound + 10) # conversion implite du booléen en entier (True => 1)

print("Le double de pi est: " + str(pi * 2)) # conversion explicite via la fonction str
triplePi = str(pi * 3)
print("Le tripe de pi est: " + triplePi)

print("Le carré de pi est: ", pi * pi) # usage de print en multi-arguments, conversion implicite
