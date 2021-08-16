# NAME: Ananya Arvind
# DATE: 5/7/2021
# PERIOD: 8
# ACTIVITY: Lab 4.01 2

# PURPOSE: translate SNAP! code to python and prints out cat song using a for loop
# INPUT: none
# OUTPUT: prints out cat song
def cat_song():
  for i in range(10, 0, -1):
    print(str(i) + " drinking milk from a saucer,")
    print(str(i) + " drinking milk from a saucer,")
    print("and if one of those cats should wander away,")
    print("there would be " + str(i) + " drinking milk from a saucer.\n")

cat_song() 