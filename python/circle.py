from math import pi

def circleArea(r):
  if type(r) not in [int, float]:
    raise TypeError("Le rayon doit être un nombre réel non négatif")
  if r < 0:
    raise ValueError("Le rayon ne peut pas être négatif")
  return pi * (r ** 2)

# test
'''
values = [4, -2, "coucou", 0]

for v in values:
  a = circleArea(v)
  print(f'Aire d\'un cercle de rayon {v}: {a}')
'''