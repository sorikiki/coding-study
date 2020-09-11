# ✅ What is a dictionaries? 
# : A dictionary is an unordered set of key: value pairs.
menu = {"oatmeal": 3, "avocado toast": 6, "carrot juice": 5, "blueberry muffin": 2}

# => However, the keys can be numbers as well.
subtotal_to_total = {20: 24, 10: 12, 5: 6, 15: 18}

# => Values can be any type. You can use a string, a number, a list, or even another dictionary as the value associated with a key!
# => ❗ but we cannot use these data types(list, dictionary) as keys of the dictionary.

# ✅ Add a Key
animals_in_zoo = {}
animals_in_zoo["zebras"] = 8
animals_in_zoo["monkeys"] = 12
animals_in_zoo["dinosaurs"] = 0
print(animals_in_zoo)

# => If we wanted to add multiple key : value pairs to a dictionary at once, we can use the .update() method.
user_ids = {"teraCoder": 9018293, "proProgrammer": 119238}

user_ids.update({"theLooper" : 138475, "stringQueen" : 85739})

print(user_ids)


# ✅ Overwrite a value(value is mutable 😊)
oscar_winners = {"Best Picture": "La La Land", "Best Actor": "Casey Affleck", "Best Actress": "Emma Stone", "Animated Feature": "Zootopia"}
oscar_winners["Best Picture"] = "Moonlight"


# ✅ List Comprehensions to Dictionaries
# : Python allows you to create a dictionary using a list comprehension, with this syntax:
names = ['Jenny', 'Alexus', 'Sam', 'Grace']
heights = [61, 70, 67, 64]

students = {key:value for key, value in zip(names, heights)}
#students is now {'Jenny': 61, 'Alexus': 70, 'Sam': 67, 'Grace': 64}

# ✅ Get a key
# - key error: when we look up to a key which is not a existed key in a dictionary.

# => methods to avoid KeyErrors
# ◽ we can avoid KeyErrors by checking if a key is in a dictionary first. 
inventory = {"iron spear": 12, "invisible knife": 30, "needle of ambition": 10, "stone glove": 20, "the peacemaker": 65, "demonslayer": 50}

print(12 in inventory) # False

# ◽ Another method we could use is a try/except:
building_heights = {"Burj Khalifa": 828, "Shanghai Tower": 632, "Abraj Al Bait": 601, "Ping An": 599, "Lotte World Tower": 554.5, "One World Trade": 541.3}

key_to_check = "Landmark 81"
try:
  print(building_heights[key_to_check])
except KeyError:
  print("That key doesn't exist!")

# ◽ Dictionaries have a .get() method to search for a value instead of the my_dict[key] notation we have been using. 
# : If the key you are trying to .get() does not exist, it will return None by default:
# => You can also specify a value to return if the key doesn’t exist.
building_heights.get('Shanghai Tower', 0)


# ✅ Delete a Key
# : .pop() works to delete items from a dictionary, when you know the key value.
available_items = {"health potion": 10, "cake of the cure": 5, "green elixir": 20, "strength sandwich": 25, "stamina grains": 15, "power stew": 30}
health_points = 20

health_points += available_items.pop("stamina grains", 0)
health_points += available_items.pop("power stew", 0)
health_points += available_items.pop("mystic bread", 0)

print(available_items)
print(health_points)
# {'health potion': 10, 'cake of the cure': 5, 'green elixir': 20, 'strength sandwich': 25}
# 65


# ✅ Get all Keys
test_scores = {"Grace":[80, 72, 90], "Jeffrey":[88, 68, 81], "Sylvia":[80, 82, 84], "Pedro":[98, 96, 95], "Martin":[78, 80, 78], "Dina":[64, 60, 75]}

# ◽ We want to get a roster of the students in the class, without including their grades. We can do this with the built-in list() function:
print(list(test_scores)) # ["Grace", "Jeffrey", "Sylvia", "Pedro", "Martin", "Dina"]

# ◽ Dictionaries also have a .keys() method that returns a dict_keys object.
# : A dict_keys object is a view object, which provides a look at the current state of the dicitonary, without the user being able to modify anything. 
# => but it can be used in the place of a list for iteration:
for student in test_scores.keys():
  print(student)

# => Dictionaries have a .values() method that returns a dict_values object (just like a dict_keys object but for values!) with all of the values in the dictionary. 
for score_list in test_scores.values():
  print(score_list) 
# => cf. There is no built-in function to get all of the values as a list, but if you really want to, you can use:
list(test_scores.values())

# => You can get both the keys and the values with the .items() method.
# : Each element of the dict_list returned by .items() is a tuple consisting of: