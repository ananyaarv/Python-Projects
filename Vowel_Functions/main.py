# NAME: Ananya Arvind
# DATE: 5/7/2021
# PERIOD: 8
# ACTIVITY: Lab 4.01

# PURPOSE: Takes in a string as input and returns a copy of that string with all of the vowels removed. If not, the string should be the same.   
# INPUT: string
# OUTPUT: returns a copy of that string with all of the vowels removed. Otherwise, the string should be the same. 
def de_vowel(a_string): 
  vowels = ['a', 'e', 'i', 'o', 'u'] 
  user_sentence = a_string 
  print(user_sentence)
  for char in vowels:
    user_sentence = user_sentence.replace(char,'',-1)
  return user_sentence  
no_vowels = de_vowel("This sentence has no vowels")
print(no_vowels)

# PURPOSE: Use a counter (variable you define outside of a loop to keep track of a value inside a loop) to create count_vowels.
# INPUT: string
# OUTPUT: integer representing the number of vowels in the string
def count_vowels(b_string):
  vowels = ['a', 'e', 'i', 'o', 'u'] 
  output = 0
  for char in vowels:
    output += b_string.count(char) 
  return output

# Examples:
no_vowels = de_vowel("Bananas are yellow.")
print(no_vowels)

no_vowels = de_vowel("I like apple pie.")
print(no_vowels)

no_vowels = de_vowel("She eats peanuts.")
print(no_vowels)

num = count_vowels ("She eats pinapple")
print(num) 


# ---------------
# | Tester Code |
# ---------------
no_vowels = de_vowel("This sentence has no vowels")
num_vowels = count_vowels("This sentence has no vowels")
print("'This sentence has no vowels' becomes: " + no_vowels)
print("It used to have " + str(num_vowels) + " vowels")
print()

no_vowels = de_vowel("Eieio")
num_vowels = count_vowels("Eieio")
print("'Eieio' becomes: " + no_vowels)
print("It used to have " + str(num_vowels) + " vowels")
print()

no_vowels = de_vowel("Rhythm")
num_vowels = count_vowels("Rhythm")
print("'Rhythm' becomes: " + no_vowels)
print("It used to have " + str(num_vowels) + " vowels")