# NAME: Ananya Arvind
# DATE: 4/19/2021
# PERIOD: 8
# ACTIVITY: Lab 3.04 

# name:add2
# prupose: add 2 to my_num
# input: None
# returns: my_num + 2
def add2():
  global my_num
  my_num+= 2

# name: multiply_num
# purpose: multiplies my_num by random parameter
# input: multiplier
# returns: my_num x multiplier 
def multiply_num(multiplier):
  global my_num
  my_num*= multiplier

# name: add2_and_multiply
# purpose: takes in parameter &  calls add2 and multiply_num 
def add2_and_multiply(multiplier):
  add2()
  multiply_num(multiplier) 

# MAIN PROGRAM
my_num= 0
print(my_num)
add2_and_multiply(8)
print(my_num)
