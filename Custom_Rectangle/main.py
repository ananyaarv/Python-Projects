# NAME: Ananya Arvind
# DATE: 5/19/2021
# PERIOD: 8
# ACTIVITY: Custom Rectangle Do Now 4.03

def rectangle( row_length,  column_length):
  for row in range(0, row_length):
    for col in range(0, (column_length)):
      print("*", end= '\t') 
    print() 

# Calling function
row_length= input("Choose a number from 1-10 for a row number:")
column_length= input("Choose a number from 1-10 for a column number:")
  
rectangle(int(row_length), int(column_length)) 