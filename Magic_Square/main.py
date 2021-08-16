# Name: Ananya Arvind
# Date: 2/19/2021
# Period: 8
# Activity: 1.2 Project

print("Welcome to Magic Square!")
number=input("Enter a number from 21 to 65:")
print("You have entered " + number + "." + "\n")

try:
  number = int(number)
except ValueError:
  print("Error. That is not an integer. I will use 33 instead.")
  number="33"
  number=int(number)
if(number<21 or number>65):
  print("Error. That is not an integer. I will use 33 instead.")
  number="33"
  number = int(number)
  print("Here is your Magic Square:")

a1 = number-20 
a2="11"
a3="5"
a4="4"
b1="1"
b2="8"
b3="10"
b4=number-19
c1="12"
c2=number-21
c3="3"
c4="6"
d1="7"
d2="2"
d3=number-18
d4="9"

print(str(a1).zfill(2) + " " + b1.zfill(2) + " " + c1.zfill(2) + " " + d1.zfill(2))
print(a2.zfill(2) + " " + b2.zfill(2) + " " + str(c2).zfill(2) + " " + d2.zfill(2))
print(a3.zfill(2) + " " + b3.zfill(2) + " " + c3.zfill(2) + " " + str(d3).zfill(2))
print(a4.zfill(2) + " " + str(b4).zfill(2) + " " + c4.zfill(2) + " " + d4.zfill(2))
