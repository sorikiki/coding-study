# ✅ Intro
# : a function is a tool that you can use over and over again to produce consistent output from different inputs.


# ✅ Write a function
# : To write a function, you must have a heading and an indented block of code.
# => The heading starts with the keyword def and the name of the function, followed by parentheses, and a colon.
# => The indented block of code performs some sort of operation.
def function_name():
    print('hello')

# - ❗ In Python, the amount of whitespace tells the computer what is part of a function and what is not part of that function. 
def greet_customer():
  print("Welcome to Engrossing Grocers.")
  print("Our special is mandarin oranges.")
  print("Have fun shopping!")
print("Cleanup on Aisle 6")
greet_customer()
greet_customer()
# => When we run this program, the message "Cleanup on Aisle 6" will be printed once, while the messages in greet_customer() will all be printed twice.


# ✅ Parameters
def greet_customer2(special_item):
  print("Welcome to Engrossing Grocers.")
  print("Our special is " + special_item + ".")
  print("Have fun shopping!")

greet_customer2("peanut butter")
# The 'special_item' is referred to as a formal parameter. 
# => This variable name is a placeholder for the name of the item that is the grocery’s special today. 

# - multiple parameters 
def mult_x_add_y(number,x,y):
  print(number*x + y)
  
mult_x_add_y(5, 2, 3)
mult_x_add_y(1, 3, 1)
# => positional parameters(because their assignments depend on their positions in the function call.)
# : Whichever value is put into greet_customer() first is assigned to grocery_store, and whichever value is put in second is assigned to special_item.

# - keyword arguments
# : we explicitly refer to what each argument is assigned to in the function call.
mult_x_add_y(number=1, x=3, y=1) # 4

# - default arguments = very similar to our keyword-argument syntax, but used during the function definition!
# => If the function is called without an argument for that parameter, it relies on the default.
def greet_customer3(special_item, grocery_store="Engrossing Grocers"):
  print("Welcome to "+ grocery_store + ".")
  print("Our special is " + special_item + ".")
  print("Have fun shopping!")
# => If we call the function with only one argument, the value of "Engrossing Grocers" is used for grocery_store:
greet_customer3("bananas")
'''
Welcome to Engrossing Grocers.
Our special is bananas.
Have fun shopping!
'''
# => Once you give an argument a default value (making it a keyword argument), no arguments that follow can be used positionally.
'''
def greet_customer(special_item="bananas", grocery_store): 
    # this is not valid
  ...

def greet_customer(special_item, grocery_store="Engrossing Grocers"):
    # this is valid
  ...
'''



# ✅ Returns
# :  Functions can also return a value to the user so that this value can be modified or used later!
# => We use the keyword 'return' to do this.
# => we could also return a String.

# - multiple return values
def square_point(x_value, y_value):
  x_2 = x_value * x_value
  y_2 = y_value * y_value
  return x_2, y_2

# => We can get those values by assigning them both to variables when we call the function:
x_squared, y_squared = square_point(1, 3)
print(x_squared) # 1
print(y_squared) # 9 


# ✅ Scope
#The variable special_item has only been defined inside the space of a function, so it does not exist outside the function.
def create_special_string(special_item):
  return "Our special is " + special_item + "."

# print("I don't like " + special_item) => error
# => We call the part of a program where special_item can be accessed its 'scope'.
# => Variables defined outside the scope of a function may be accessible inside the body of the function.

def current_age(current_year, birth_year) {
    age = current_year - birth_year
    return age
}

# print(current_year) => error
# print(age) => error

