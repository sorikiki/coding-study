# ✅ Parameters and Arguments
# ◽ A parameter is a variable in the definition of a function.
# ◽ An argument is the value being passed into a function call.
# ◽ A function definition begins with def and contains the entire following indented block.
# ◽ And function calls are the places a function is invoked, with parentheses, after its definition


# ✅ None: it's nothing!
# => None is a special value in Python. It is unique (there can’t be two different Nones) and immutable (you can’t update None or assign new attributes to it).
none_var = None
if none_var:
  print("Hello!")
else:
  print("Goodbye")

# Prints "Goodbye"
# => None is falsy, meaning that it evaluates to False in an if statement, which is why the above code prints “Goodbye”. 
# => None is also unique, which means that you can test if something is None using the is keyword.


# ✅ Default Return
# : A Python function that does not have any explicit return statement will return None after completing. 
# => This means that all functions in Python return something, whether it’s explicit or not.
# => We can simply write 'return' instead of 'return None'
sort_this_list = [14, 631, 4, 51358, 50000000]

list_sort_return = sort_this_list.sort()


# print out the value of list_sort_return
print(list_sort_return)
# None
# => It might be surprising, but .sort() sorts a list in place. Python has a different function, sorted() that takes a list as an argument and returns the sorted list.


# ✅ Default Values
'''
# Function defined with one required and one optional parameter
def create_user(username, is_admin=False):
  create_email(username)
  set_permissions(is_admin)

# Calling with two arguments uses the default value for is_admin
user2 = create_user('djohansen')
'''
'''
# We can make all three parameters optional
def create_user(username=None, is_admin=False):
  if username is None:
    username = "Guest"
  else:
    create_email(username)
  set_permissions(is_admin)

# So we can call with just one value
user3 = create_user('ssylvain')
# Or no value at all, which would create a Guest user
user4 = create_user()
'''

# ❗ The required parameters need to occur before any parameters with a default argument.


# ✅ Keyword Arguments
# : We use keyword arguments by passing arguments to a function with a special syntax that uses the names of the parameters.
# =>  This is useful if the function has many optional default arguments or if the order of a function’s parameters is hard to tell.
# => cf. Changing the arguments to be keyword parameters means taking away the curly braces, passing the keys without quotes, and using = instead of :


# ✅ Don't use mutable default arguments
def populate_list(list_to_populate=[], length=1):
  for num in range(length):
    list_to_populate.append(num)
  return list_to_populate
# => It’s reasonable to believe that list_to_populate will be given an empty list every time it’s called.
# => However, it's not the case.
# => list_to_populate will be given a new list once, in its definition, and all subsequent function calls will modify the same list. 
returned_list = populate_list(length=4)
print(returned_list)
# Prints [0, 1, 2, 3] -- this is expected

returned_list = populate_list(length=6)
print(returned_list)
# Prints [0, 1, 2, 3, 0, 1, 2, 3, 4, 5] -- this is a surprise!
# => This result is caused by the fact that 'list' is mutable object.
# => A list has append and remove operations that change the nature of a list. Sets and dictionaries are two other mutable objects in Python.

# cf. It might be helpful to note some of the objects in Python that are not mutable (and therefore OK to use as default arguments). 
# ◽ int, float, and other numbers can’t be mutated (arithmetic operations will return a new number).
# ◽ tuples are a kind of immutable list.
# ◽ Strings are also immutable.


# ✅ Using None as a sentinel
# ❓ So if we can’t use a list as a default argument for a function, what can we use? 
# => if we want an empty list, we can use None as a special value to indicate we did not receive anything. 
# => After we check whether an argument was provided we can instantiate a new list if it wasn’t.
# =>✨ This way multiple calls to add_author won’t include data from previous calls to add_author. 
def add_author(authors_books, current_books=None):
  if current_books is None:
    current_books = []

  current_books.extend(authors_books)
  return current_books


# ✅ Unpacking Multiple Returns
def multiple_returns(cool_num1, cool_num2):
  sum_nums = cool_num1 + cool_num2
  div_nums = cool_num1 / cool_num2
  return sum_nums, div_nums

sum_and_div = multiple_returns(20, 10)

print(sum_and_div)
# Prints "(30, 2)"

print(sum_and_div[0])
# Prints "30"
# => So we get those two values back in what’s called a tuple, an immutable list-like object indicated by parentheses. 
# => We can save these two results in seperate variables by unpacking the function return. 
'''
sum, div = sum_and_div(18, 9)

print(sum)
# Prints "27"

print(div)
# Prints "2"
'''


# ✅ Positional Argument Unpacking
# ❓ We don’t always know how many arguments a function is going to receive, and sometimes we want to handle any possibility that comes at us. 
# => The first method is called positional argument unpacking, because it unpacks arguments given by position. Here’s what that looks like:
def shout_strings(*args):
  for argument in args:
    print(argument.upper())

shout_strings("hi", "what do we have here", "cool, thanks!")
# Prints out:
# "HI"
# "WHAT DO WE HAVE HERE"
# "COOL, THANKS!"
# => In shout_strings() we use a single asterisk (*) to indicate we’ll accept any number of positional arguments passed to the function.
# => Our parameter args is a tuple of all of the arguments passed.
# => Note that args is just a parameter name, and we aren’t limited to that name (although it is rather standard practice). 


# ✅ Keyword Argument Unpacking 
# : The syntax is very similar, but uses two asterisks (**) instead of one. 
# + Instead of args, we call this kwargs — as a shorthand for keyword arguments.
# 
'''
from products import create_product

# Update create_products() to take arbitrary keyword arguments
def create_products(**products_dict):
  for name, price in products_dict.items():
    create_product(name, price)

# Checkpoint 3
# Update the call to `create_products()` to pass in this dictionary as a series of keyword
create_products(
  Baseball='3',
  Shirt='14',
  Guitar='70')
'''

# ✅ Using Both Keyword and Positional Unpacking
# : You should conform to this rule.
# => the parameters must be listed in this order:
# ◽ All named positional parameters
# ◽ An unpacked positional parameter (*args)
# ◽ All named keyword parameters
# ◽ An unpacked keyword parameter (**kwargs)


# ✅ Passing Containers as Arguments: deconstructuring ✨
# : Not only can we accept arbitrarily many parameters to a function in our definition, but Python also supports a syntax that makes deconstructing any data that you have on hand to feed into a function that accepts these kinds of unpacked arguments.
def takes_many_args(*args):
  print(','.join(args))

long_list_of_args = [145, "Mexico City", 10.9, "85C"]

# We can use the asterisk "*" to deconstruct the container.
# This makes it so that instead of a list, a series of four different
# positional arguments are passed to the function
takes_many_args(*long_list_of_args)
# Prints "145,Mexico City,10.9,85C"

# - Similarly we can use ** to destructure a dictionary.
# def pour_from_sink(temperature="Warm", flow="Medium"):
#   set_temperature(temperature)
#   set_flow(flow)
#   open_sink()

# Our function takes two keyword arguments
# If we make a dictionary with their parameter names...
sink_open_kwargs = {
  'temperature': 'Hot',
  'flow': "Slight",
}

# We can destructure them an pass to the function
# pour_from_sink(**sink_open_kwargs)
# Equivalent to the following:
# pour_from_sink(temperature="Hot", flow="Slight")

# => We can use this destructuring syntax even when the function has a specific number of keyword or positional arguments it accepts.
# => We just need to be careful that the object we’re destructuring matches the length (and names, if a dictionary) of the signature of the function we’re passing it into.
