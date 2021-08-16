# Name: Ananya Arvind
# Date: 3/12/2021
# Period: 8
# Activity: Lab 2.05

a=input("Select a spot on the board to change:")
print("Instead of the number you chose, there will be an X on the spot.")
b=['1', '2', '3'] 
c=['4', '5', '6']
d=['7', '8', '9']
a=int(a) 
if (a==1):
  b[0] = 'X'
elif (a==2):
  b[1] = 'X'
elif (a==3):
  b[2] = 'X'
elif (a==4):
  c[0] = 'X'
elif (a==5): 
  c[1] = 'X'
elif (a==6): 
  c[2] = 'X'
elif (a==7): 
  d[0] = 'X'
elif (a==8):
  d[1] = 'X'
elif (a==9):
  d[2] = 'X'
print(b)
print(c)
print(d)