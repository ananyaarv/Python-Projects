# NAME: Ananya Arvind 
# DATE: 3/10/2021
# PERIOD: 8
# ACTIVITY: Lab 2.04 Part 2

# DO NOT CHANGE THE CODE ON LINES 7-17
# food = ['donuts', 'pancakes', 'bacon', 'waffles','eggs','bagels']
# score = [0,0,0,0,0,0]

# print("Answers will be taken as 'y' or 'n'.")

# user_input = input("Do you like food with holes? ")

# if user_input == 'y':
  # score[0] = score[0] + 1
  # score[5] = score[5] + 1
# YOUR CODE BEGINS BELOW THIS LINE

food= ['skittles', 'gummy bear', 'twix', 'star burst', 'snicker', 'airhead']
score = [0,0,0,0,0,0]
print("Answers will be taken as 'y' or 'n'.")
user_input = input("Do you like chocolate?")
if user_input == 'y':
  score[2]= score[2] +1
  score[4]= score[4] +1 
user_input = input("Do you like sour candy?")
if user_input == 'y':
  score[0]= score[0] +1
  score[5]= score[5] +1
user_input = input("Do you like little candies?")
if user_input == 'y':
  score[0]= score[0]+1
  score[1]= score[1]+1
  score[3]= score[3]+1
user_input = input("Do you like hard to chew candies?")
if user_input == 'y':
  score[1]= score[1]+1
  score[3]= score[3]+1
  score[5]= score[5]+1
user_input = input("Do you like crunchy candies?")
if user_input == 'y':
  score[2]= score[2]+1
  score[4]= score[4]+1
user_input = input("Do you like sticky candy?")
if user_input == 'y':
  score[2]= score[2]+1
  score[4]= score[4]+1
user_input = input("Do you like caramel in your candy?")
if user_input == 'y':
  score[2]= score[2]+1
  score[4]= score[4]+1
user_input = input("Do you like sweet candy?")
if user_input == 'y':
  score[0]= score[0]+1
  score[1]= score[1]+1
  score[3]= score[3]+1
print(score) 
max_value=max(food) 
print(max(food)) 