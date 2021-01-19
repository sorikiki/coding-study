# ✅ String: A string can be thought of as a list of characters. 😀
# - Selecting: indices of a string also start at 0. (❗ It’s important to note that indices of strings must be integers. Otherwise, it throws type-error)
# - Slicing: We can also select entire chunks of characters from a string.
# - Concatenating 

# Note that each time we perform one of these operations we are creating an entirely new string.
# => This is because strings are 'immutable'.
first_name = "Bob"
last_name = "Daily"

# first_name[0] = "R" => Error

fixed_first_name = "R" + first_name[1:] 

print(fixed_first_name)


# ✅ Escaping Characters
# : By adding a backslash in front of the special character we want to escape, \", we can include it in a string.
favorite_fruit_conversation = "He said, \"blueberries are my favorite!\""
# ❕ "\" is also a special character so we use this like "\\"

# ✅ Is there a certain 'character or string' in the word? => use 'in' keyword!
def contains(big_string, little_string):
  return little_string in big_string

def common_letters(string_one, string_two):
  array = []
  for character in string_one:
    if character in string_two:
      if not(character in array):
        array.append(character)
  return array

print(common_letters('apple', 'elephant'))


# ✅ String Methods
# ◽ Formatting 
# - .lower() returns the string with all lowercase characters.
# - .upper() returns the string with all uppercase characters.
# - .title() returns the string in title case, which means the first letter of each word is capitalized.
# => ❗ Note that string methods can only create new strings, they do not change the original string.

# ◽ Splitting (string -> list)
# - .split() is performed on a string, takes one argument, and returns a list of substrings found between the given argument (which in the case of .split() is known as the delimiter). 
# => If you do not provide an argument for .split() it will default to splitting at spaces.
greatest_guitarist = "santana"
greatest_guitarist_fixed = greatest_guitarist.split('a') # ['s', 'nt', 'n', ' ']
# => ❗ Note that there is an unexpected extra '' string in this list. When you split a string on a character that it also ends with, you’ll end up with an empty string at the end of the list.

# - We can also split strings using escape sequences. (\n: NewLine, \t: Horizontal Tab)
smooth_chorus = \
"""And if you said, "This life ain't good enough."
I would give my world to lift you up
I could change my life to better suit your mood
Because you're so smooth"""

chorus_lines = smooth_chorus.split('\n')

print(chorus_lines) # ❕ ['And if you said, "This life ain\'t good enough."', 'I would give my world to lift you up', 'I could change my life to better suit your mood', "Because you're so smooth"] ❕
# Be careful, how elements of a new list seem to us. Also, notice that Python automatically escaped the ' character when it created the new list.

# ◽ Joining (Don't forget this method is a subset of string methods.)
# - .join() is essentially the opposite of .split(), it joins a list of strings together with a given delimiter.
# => It is weird because with .split() the argument was the delimiter, but now the argument is the list.
# => This means that The string .join() acts on is the delimiter you want to join with, therefore the list you want to join has to be the argument.
my_munequita = ['My', 'Spanish', 'Harlem', 'Mona', 'Lisa']
my_munequita_fixed = ' '.join(my_munequita)
print(my_munequita_fixed) # 'My Spanish Harlem Mona Lisa'

# ◽ Stripping
# - Stripping a string removes all whitespace characters from the beginning and end.
# => You can also use .strip() with a character argument, which will strip that character from either end of the string.

# ◽ Replacing
# - Replace takes two arguments and replaces all instances of the first argument in a string with the second argument.

# ◽ Finding
# - .find() takes a string as an argument and searching the string it was run on for that string.
# => It then returns the first index value where that string is located.

# ◽ Inserting
# - .format() takes variables as an argument and includes them in the string that it is run on.
# => You include {} marks as placeholders for where those variables will be imported.
# => Note: .format() can take as many arguments as there are {} in the string it is run on.
def favorite_song_statement(song, artist):
  return "My favorite song is {} by {}.".format(song, artist)

print(favorite_song_statement("Smooth", "Santana")) # "My favorite song is Smooth by Santana"

# - remove ambiguity: .format() can be made even more legible for other people reading your code by including keywords.
# => By including keywords in the string and in the arguments, you can remove that ambiguity. 
def favorite_song_statement2(song, artist):
    return "My favorite song is {song} by {artist}.".format(song=song, artist=artist)

def poem_description(publishing_date, author, title, original_work):
  poem_desc = "The poem {title} by {author} was originally published in {original_work} in {publishing_date}.".format(publishing_date=publishing_date, author=author, title=title, original_work=original_work)
  return poem_desc

my_beard_description = poem_description(author = "Shel Silverstein",
title = "My Beard",
original_work = "Where the Sidewalk Ends",
publishing_date = "1974")

print(my_beard_description)


