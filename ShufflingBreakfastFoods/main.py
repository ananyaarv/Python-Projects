# Name: Ananya Arvind
# Date: 4/7/2021
# Period: 8
# Activity: Lab 3.01 Part 1

import random
a=input("There is a dice. Would you like to roll it?")
if a=="yes":
  random.randint(1, 6)
  print(random.randint(1, 6))
if a=="no":
  print("Whatever. I'm still going to roll the dice.")
  random.randint(1,6)
  print("I roled", random.randint(1, 6))

b=input("\nI'm going to role a dice. Would you like to see what number I role?")
if b=="yes":
  random.randint(1, 6)
  print(random.randint (1, 6))
if b=="no":
  print("Well too bad. I'm going to show you anyway.")
  random.randint(1, 6)
  print("I roled", random.randint(1, 6))

c=["eggs", "bacon", "toast", "pancakes", "orange juice", "sausage"]
print("\nI am going to shuffle a list of breakfast food items")
random.shuffle(c)
print(c) 