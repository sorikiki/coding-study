# ✅ variable
# ◽ rule
# - Variables can’t have spaces or symbols in their names other than an underscore (_).
# - They can’t begin with numbers but they can have numbers after the first letter (e.g., cool_variable_5 is OK).

# ✅ data types
# ◽ int
# ◽ float
an_int = 2
a_float = 2.1

print(an_int + 3) # prints 5
# cf. We call the number 3 here a literal, meaning it’s actually the number 3 and not a variable with the number 3 assigned to it.


# ✅ operators

# ◽ "+,-,*,/"

# Prints "500"
print(573 - 74 + 1)

# Prints "50"
print(25 * 2)

# Prints "2.0"
print(10 / 5)
# => Notice that when we perform division, the result has a decimal place. This is because Python converts all ints to floats before performing division.

# ◽ "**" (exponentiation)

# 9 * 9 * 9, 9 cubed, or 729
print(9 ** 3)

# We can even perform fractional exponents
# 4 to the half power, or 2
print(4 ** 0.5)

# ◽ Modulo("%")
# : The modulo operator is indicated by % and gives the remainder of a division calculation.

# Prints 4 because 29 / 5 is 5 with a remainder of 4
print(29 % 5)

# Prints 2 because 32 / 3 is 10 with a remainder of 2
print(32 % 3)

# Modulo by 2 returns 0 for even numbers and 1 for odd numbers
# Prints 0
print(44 % 2)

# ◽ Concatenation

# : The + operator doesn’t just add two numbers, it can also “add” two strings!
greeting_text = "Hey there!"
question_text = "How are you doing?"
full_text = greeting_text + question_text

# Prints "Hey there!How are you doing?"
print(full_text)

#  let’s add the space in-between using the same concatenation operator!
full_text = greeting_text + " " + question_text

# Prints "Hey there! How are you doing?"
print(full_text)

# If you want to concatenate a string with a number you will need to make the number a string first, using the str() function.
birthday_string = "I am "
age = 10
birthday_string_2 = " years old today!"

# Concatenating an integer with strings is possible if we turn the integer into a string first
full_birthday_string = birthday_string + str(age) + birthday_string_2

# Prints "I am 10 years old today!"
print(full_birthday_string)

# But we don’t need to convert a number to a string for it to be an argument to a print statement.

# This also prints "I am 10 years old today!"
print(birthday_string, age, birthday_string_2)

# ◽ Plus Equals("+=")
# : When you have a number saved in a variable and want to add to the current value of the variable, you can use the += (plus-equals) operator.

# The plus-equals operator also can be used for string concatenation, like so:
hike_caption = "What an amazing time to walk through nature!"

# Almost forgot the hashtags!
hike_caption += " #nofilter"
hike_caption += " #blessed"

# ◽ Multi-line Strings
# : if we try to create a string that occupies multiple lines we find ourselves face-to-face with a SyntaxError. 
# =>  By using three quote-marks (""" or ''') instead of one, we tell the program that the string doesn’t end until the next triple-quote.
leaves_of_grass = """
Poets to come! orators, singers, musicians to come!
Not to-day is to justify me and answer what I am for,
But you, a new brood, native, athletic, continental, greater than
  before known,
Arouse! for you must justify me.
"""

# ❗ If a multi-line string isn’t assigned a variable or used in an expression it is treated as a comment.

# 👏 So far, we’ve covered how to assign variables values directly in a Python file. 
# => However, we often want a user of a program to enter new information into the program.
# => While we output a variable’s value using print(), we assign information to a variable using input(). 
# => The input() function requires a prompt message, which it will print out for the user before they enter the new information.
likes_snakes = input("Do you like snakes? ")

'''
In the example above, the following would occur:

The program would print “Do you like snakes? “ for the user.
The user would enter an answer (e.g., “Yes! I have seven pythons as pets!”).
The variable likes_snakes would be assigned a value of the user’s answer (in this case, “Yes! I have seven pythons as pets!”).
'''