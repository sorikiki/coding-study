# ✅ What is a module?
# - A module is a collection of Python declarations intended broadly to be used as a tool. 
# => Modules are also often referred to as “libraries” or “packages”
# => cf. a package is really a directory that holds a collection of modules.
# => Usually, to use a module in a file, the basic syntax you need at the top of that file is:
# ex. from module_name import object_name

# - One common library that comes as part of the Python Standard Library is datetime. 
# => datetime helps you work with dates and times in Python.
# =>  In this case, you’ll notice that datetime is both the name of the library and the name of the object that you are importing. 😊
from datetime import datetime
current_time = datetime.now()
print(current_time) # 2020-09-06 07:18:04.065878

# - Another one of the most commonly used is random which allows you to generate numbers or select items at random.
# => We’ll work with two common random functions:
# 1. random.choice() which takes a list as an argument and returns a number from the list
# 2. random.randint() which takes two numbers as arguments and generates a random number between the two numbers you passed in
# Import random below:
# 3. random.sample() that takes a range and a number as its arguments. It will return the specified number of random numbers from that range.
import random

# Create random_list below:
random_list = [random.randint(1,101) for i in range(101)]

# Create randomer_number below:
randomer_number = random.choice(random_list)

# Print randomer_number below:
print(randomer_number)


# ✅ Modules Python NameSpace
# : A namespace isolates the functions, classes, and variables defined in the module from the code in the file doing the importing.
# => Python defaults to naming the namespace after the module being imported.
# => However, sometimes this name could be ambiguous or lengthy.
# => Fortunately, this name can be altered by aliasing using the as keyword:
# ex. import module_name as name_you_pick_for_the_module
'''
import codecademylib3_seaborn
from matplotlib import pyplot as plt
import random
# Add your code below:
numbers_a = range(1, 13)
numbers_b = random.sample(range(1000), 12)

plt.plot(numbers_a, numbers_b)
plt.show()
'''


# ✅ Modules Python Decimals
# - If you used Python’s built-in floating-point arithmetic to calculate a sum, it would result in a weirdly formatted number.
cost_of_gum = 0.10
cost_of_gumdrop = 0.35

cost_of_transaction = cost_of_gum + cost_of_gumdrop
# Returns 0.44999999999999996
# => from decimal import Decimal
'''
cost_of_gum = Decimal('0.10')
cost_of_gumdrop = Decimal('0.35')

cost_of_transaction = cost_of_gum + cost_of_gumdrop
# Returns 0.45 instead of 0.44999999999999996
'''


# ✅ Modules Python Files and Scope
# - Scope also applies to classes and to the files you are working within, not only to functions.
# => Even files inside the same directory do not have access to each other’s variables, functions, classes, or any other code.
# ❓ So if I have a file sandwiches.py and another file hungry_people.py, how do I give my hungry people access to all the sandwiches I defined?
# ❗ Since files are actually modules, so you can give a file access to another file’s content using that glorious import statement.
# => ex. from sandwiches import sandwiches


# ✅ Virtual environments
# ❓ If application A needs version 1.0 of a particular module but application B needs version 2.0, then the requirements are in conflict and installing either version 1.0 or 2.0 will leave one application unable to run.
# => The solution for this problem is to create a virtual environment, a self-contained directory tree that contains a Python installation for a particular version of Python, plus a number of additional packages.