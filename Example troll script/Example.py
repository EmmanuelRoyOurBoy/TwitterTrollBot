import random
Wordstotroll=input("What phrase do you want to trollify?)
def Troll(text)
  new = []
  for c in text:
    r = random.randint(0,1)
    if r:
        new.append(c.upper())
    else:
      new.append(c.lower())
  return
print(Troll(Wordstotroll)
