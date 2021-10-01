from random import randint

proverbs = [
  "Il ne faut pas vendre la peau de l'ours avant de l'avoir tué",
  "Omnia labor vincit",
  "Tra il dire e il fare c'è in mezzo il mare",
  "Ad astra per aspera",
  "An apple a day keeps the doctor away",
  "Un tiens vaut mieux que deux tu l'auras"
]

indexMax = len(proverbs) - 1
randomIndex = randint(0, indexMax)
print(proverbs[randomIndex])