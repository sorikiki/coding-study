# ✅ for loop (❗ indentation) 
'''
for <temporary variable> in <list variable>:
✔✔✔ <action>
'''
# => ex. In our dog breeds example, breed was the temporary variable, dog_breeds was the list variable, and print(breed) was the action performed on every item in the list.
dog_breeds = ['french_bulldog', 'dalmatian', 'shihtzu', 'poodle', 'collie']

for breed in dog_breeds:
    print(breed)

# - range():Often we won’t be iterating through a specific list, we’ll just want to do a certain action n times. 
# => To create these lists of length n, we can use the 'range' function.

# - break: You can stop a for loop from inside the loop by using break. 
# => When the program hits a break statement, control returns to the code outside of the for loop.

# - continue: When we’re iterating through lists, we may want to skip some values.
# => the continue keyword moved the index to the next value in the list, without executing the code in the rest of the for loop.


# ✅ while loop: The while loop performs a set of code until some condition is reached.
# => While loops can be used to iterate through lists, just like for loops.
index = 0
while index < len(dog_breeds):
  print(dog_breeds[index])
  index += 1


# ✅ Nested loop 
sales_data = [[12, 17, 22], [2, 10, 3], [5, 12, 13]]

scoops_sold = 0
for location in sales_data:
  for i in location:
    scoops_sold += i

print(scoops_sold)


# ✅ List Comprehensions
# : Create a new list based on the original list.✨

# ex1. We want to make a new list, called usernames, that has all of the strings in words with an '@' as the first character. 

words = ["@coolguy35", "#nofilter", "@kewldawg54", "reply", "timestamp", "@matchamom", "follow", "#updog"]
usernames = []

for word in words:
  if word[0] == '@':
    usernames.append(word)

# => Let's use List Comprehensions
usernames2 = [word for word in words if word[0] == '@']
'''
1. Takes an element in words
2. Assigns that element to a variable called word
3. Checks if word[0] == '@', and if so, it adds word to the new list, usernames. If not, nothing happens.
4. Repeats steps 1-3 for all of the strings in words
'''

# ex2. We want to create a new list with the string " please follow me!" added to the end of each username. 
messages = [user + " please follow me!" for user in usernames2]
'''
1. Takes a string in usernames
2. Assigns that string to a variable called user
3. Adds “ please follow me!” to user
4. Appends that concatenation to the new list called messages
5. Repeats steps 1-4 for all of the strings in usernames
'''