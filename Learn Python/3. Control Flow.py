# ✅ Relational Operators 
# ◽ equals, not equals
'''
>>> 1 == 1
True
>>> 2 != 4
True
>>> 3 == 5
False
>>> '7' == 7
False
'''
# => When using relational operators it is important to always be mindful of type.

# ◽ >,<,>=,<=

# ✅ data types: boolean
# - True and False are the only bool types, and any variable that is assigned one of these values is called a boolean variable. 
# - Boolean values True and False always need to be capitalized and do not have quotation marks.

my_baby_bool = "true"
print(type(my_baby_bool))

my_baby_bool_two = True
print(type(my_baby_bool_two))


# ✅ Boolean Operators(and, or, not)
# Javascript=> Python
# && => and
# || => or
# ! => not


# ✅ if, else, elif
# - An elif statement checks another condition after the previous if statements conditions aren’t met.
def grade_converter(gpa):
  grade = "F"
  
  if gpa >= 4.0:
    grade = "A"
  elif gpa >= 3.0:
    grade = "B"
  elif gpa >= 2.0:
    grade = "C"
  elif gpa >= 1.0:
    grade = "D"
    
  return grade


# ✅ try, except
'''
try:
    # some statement
except ErrorName:
    # some statement
'''
#  If at some point an exception is raised during this execution, such as a NameError or a ValueError and that exception matches the keyword in the except statement, then the try statement will terminate and the except statement will execute.
def divides(a,b):
  try:
    result = a / b
    print (result)
  except ZeroDivisionError:
    print ("Can't divide by zero!")

def raises_value_error():
  raise ValueError
  
try:
  raises_value_error()
except ValueError:
  print("You raised a ValueError!") # You raised a ValueError!
  
