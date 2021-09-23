# Module Tools
import random

def example():
  random.randint(0,10)
  print("Simple exemple")

def separator(character, times = 50):
  row = ""
  for n in range(times):
    row += character
  print(row)

def randSeparator(times = 50):
  character = random.choice(["*","-","_","#"])
  row = ""
  for n in range(times):
    row += character
  print(row)