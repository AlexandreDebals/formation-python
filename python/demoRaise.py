def demo(n):
  if n > 10:
    raise ValueError("n ne peut pas être supérieur à 10")

demo(5)

#demo(11)

try:
  demo(11)
except ValueError:
  print("Mauvaise valeur fournie entrée...")
except:
  print("Le programme a rencontré une erreur.")

print("The end...")
