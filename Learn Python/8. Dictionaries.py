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