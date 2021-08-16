# Name: Ananya Arvind
# Date: 3/10/2021
# Period: 8
# Activity: Lab 2.04 Part 1

prize=['A Pepsi', 'A Root Beer', 'A Mountain Dew', 'A Sierra Mist', 'A Water Bottle', 'A Coca-Cola', 'A Doctor Pepper', 'A Lemonade', 'A Sunny D', 'A Fanta']
userinput=input("Pick a number from 1 to 10:")
userinput= int(userinput) 
if(userinput<1 or userinput>10): 
  print("That is not in between 1 and 10. You get no prize!")
else:
  print(prize[userinput - 1]) 