# ✅ List: A list is an ordered set of objects in Python.
# - We can also combine multiple data types in one list. 
# - We can put several of lists into one list, such that each entry in the list represents a student and their height:
collabo = [['Jenny', 61], ['Alexus', 70], ['Sam', 67], ['Grace', 64]]


# ✅ Zip: zip takes two (or more) lists as inputs and returns an object that contains a list of pairs.
names = ['Jenny', 'Alexus', 'Sam', 'Grace']
heights = [61, 70, 67, 65]
names_and_heights = zip(names, heights)
print(names_and_heights) # <zip object at 0x7f1631e86b48>

# To see the nested lists, you can convert the zip object to a list first:
print(list(names_and_heights)) # [('Jenny', 61), ('Alexus', 70), ('Sam', 67), ('Grace', 65)]


# ✅ Growing a List
# ◽ append(❗ you can assign only one element to an array): It’s important to remember that .append() comes after the list. = javascript's array built-in method 'push'
# ◽ plus(+)
items_sold = ['cake', 'cookie', 'bread']
items_sold_new = items_sold + ['biscuit', 'tart']
print(items_sold_new) # ['cake', 'cookie', 'bread', 'biscuit', 'tart']

my_list = [1, 2, 3]
# my_list + 4 => if we want to add a single element using +, we have to put it into a list with brackets ([])
my_list + [4] # => this is valid.


# ✅ Range
# : Often, we want to create a list of consecutive numbers. 
# => The function 'range' takes a single input, and generates numbers starting at 0 and ending at the number before the input by default.
# => ex. So, if we want the numbers from 0 through 9, we use range(10) because 10 is 1 greater than 9
my_range = range(10)
print(my_range) # range(0, 10)
print(list(my_range)) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# - However, if we call range with two arguments, we can create a list that starts at a different number.
# => For example, range(2, 9) would generate numbers starting at 2 and ending at 8 (just before 9)

# - If we use a third argument, we can create a list that “skips” numbers.
# => ex. range(2, 9, 2) will give us a list where each number is 2 greater than the previous number.
my_range2 = range(2, 9, 2)
print(list(my_range2))
[2, 4, 6, 8]


# ✅ Length of a List(len)
my_list = [1, 2, 3, 4, 5]
print(len(my_list))


# ✅ Selecting an element by index(= this is same with javascript.)
# it starts from 0
# We can use the index -1 to select the last item of a list, even when we don’t know how many elements are in a list.


# ✅ Slicing Lists(= this is same with javascript's built-in array method 'slice')
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
letters[0:3] # ['a','b','c']

# - When starting at the beginning of the list, it is also valid to omit the 0:
fruits = ['apple', 'banana', 'cherry', 'date']
print(fruits[:3])

# - We can do something similar when selecting the last few items of a list:
print(fruits[2:]) # ['cherry' , 'date']

# - If we want to select the last 3 elements of fruits, we can also use this syntax:
print(fruits[-3:]) # ['banana', 'cherry', 'date']


# ✅ Counting elements
letters = ['m', 'i', 's', 's', 'i', 's', 's', 'i', 'p', 'p', 'i']
num_i = letters.count('i')
print(num_i) # 4


# ✅ Sorting Lists
# ◽ 1. sort()
# - Notice that sort goes after our list, names
# - sort does not return anything
names = ['Xander', 'Buffy', 'Angel', 'Willow', 'Giles']
names.sort()
print(names)

# ◽ 2. sorted
# - vs sort(): It comes before a list, instead of after.
# => Moreover, it generates a new list.
sorted_names = sorted(names)
print(sorted_names) # ['Angel', 'Buffy', 'Giles', 'Willow', 'Xander'] => alphabetically





