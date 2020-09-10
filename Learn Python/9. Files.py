# ✅ Read a file
# ◽ .read()
with open('real_cool_document.txt') as cool_doc:
  cool_contents = cool_doc.read()
print(cool_contents)
# => Here 'cool_contents' is not a local variable.

# ◽ .readlines()
# => what if we wanted to store each line in a variable? 
# : We can use the .readlines() function to read a text file line by line instead of having the whole thing.
with open('how_many_lines.txt') as lines_doc:
  for line in lines_doc.readlines():
    print(line)

# ◽ .readline()
# => there’s a different file method, .readline(), which will only read a single line at a time. 


# ✅ Create a file
# script.py
with open('generated_file.txt', 'w') as gen_file:
  gen_file.write("What an incredible file!")
# => Here we pass the argument 'w' to open() in order to indicate to open the file in write-mode.
# => The default argument is 'r' and passing 'r' to open() opens the file in read-mode as we’ve been doing.
# => This code creates a new file in the same folder as script.py and gives it the text What an incredible file!
# => It’s important to note that if there is already a file called generated_file.txt it will completely overwrite that file, erasing whatever its contents were before.


# ✅ Appending to a File
# ❓ Isn’t there a way to just add a line to a file without completely deleting it?
# ❗ Instead of opening the file using the argument 'w' for write-mode, we open it with 'a' for append-mode.
# generated_file.txt
# This was a popular file...

# script.py
with open('generated_file.txt', 'a') as gen_file:
  gen_file.write("... and it still is")

# generated_file.txt
# This was a popular file...
# ... and it still is

# => If we were to run script.py again, this would be what generated_file.txt looks like:
# generated_file.txt
# This was a popular file...
# ... and it still is
# ... and it still is


# ✅ What the roles of 'with'? 
# : The 'with' keyword invokes something called a context manager for the file that we’re calling open() on.
# => This context manager takes care of opening the file when we call open() and then closing the file after we leave the indented block.

# ❓ Why is closing the file so complicated? 
'''
A. Since your files exist outside your Python script, we need to tell Python when we’re done with them so that it can close the connection to that file.
Leaving a file connection open unnecessarily can affect performance or impact other programs on your computer that might be trying to access that file.
The with syntax replaces older ways to access files where you need to call .close() on the file object manually.
'''

# This is an old way before 'with' syntax comes to us. 🤔
fun_cities_file = open('fun_cities.txt', 'a')

# We can now append a line to "fun_cities".
fun_cities_file.write("Montréal")

# But we need to remember to close the file
fun_cities_file.close()


# ✅ What is a CSV File
# - Text files aren’t the only thing that Python can read, but they’re the only thing that we don’t need any additional parsing library to understand. 🤔
# => 'CSV files' are an example of a text file that impose a structure to their data.
# => CSV stands for Comma-Separated Values and CSV files are usually the way that data from spreadsheet software (like Microsoft Excel or Google Sheets) is exported into a portable format. 


# ✅ Reading a CSV File
# - We can read CSV files without parsing contents, but there are ways to access the data in a format better suited for programming purposes.
# => In Python we can convert that data into a dictionary using the csv library’s DictReader object. 
import csv

list_of_email_addresses = []
with open('users.csv', newline='') as users_csv:
  user_reader = csv.DictReader(users_csv)
  for row in user_reader:
    list_of_email_addresses.append(row['Email'])
# ✔ In the above code we first import our csv library, which gives us the tools to parse our CSV file. 
# ✔ We pass the additional keyword argument newline='' to the file opening open() function so that we don’t accidentally mistake a line break in one of our data fields as a new row in our CSV.
# => The possibility of a new line escaped by a \n character in our data is why we pass the newline='' keyword argument to the open() function.
# ✔ After opening our new CSV file we use csv.DictReader(users_csv) which converts the lines of our CSV file to Python dictionaries which we can use access methods for.
# => When we iterate through the rows of our user_reader object, we access all of the rows in our CSV as dictionaries (except for the first row, which we used to label the keys of our dictionary).


# ✅ Reading different types of CSV Files
# - We’ve been acting like CSV files are Comma-Separated Values files. It’s true that CSV stands for that, but it’s also true that other ways of separating values are valid CSV files these days.
import csv

with open('addresses.csv', newline='') as addresses_csv:
  address_reader = csv.DictReader(addresses_csv, delimiter=';')
  for row in address_reader:
    print(row['Address'])
# => Although 'addresses.csv' file has many commas, we’ll still be able to read it. 
# => Notice that when we call csv.DictReader we pass in the delimiter parameter, which is the string that’s used to delineate separate fields in the CSV. 😊


# ✅ Writing a CSV File
big_list = [{'name': 'Fredrick Stein', 'userid': 6712359021, 'is_admin': False}, {'name': 'Wiltmore Denis', 'userid': 2525942, 'is_admin': False}, {'name': 'Greely Plonk', 'userid': 15890235, 'is_admin': False}, {'name': 'Dendris Stulo', 'userid': 572189563, 'is_admin': True}] 

import csv

with open('output.csv', 'w') as output_csv:
  fields = ['name', 'userid', 'is_admin']
  output_writer = csv.DictWriter(output_csv, fieldnames=fields)

  output_writer.writeheader()
  for item in big_list:
    output_writer.writerow(item)


# ✅ Reading a JSON file.

# : CSV isn’t the only file format that Python has a built-in library for. We can also use Python’s file tools to read and write JSON. 😊
# purchase_14781239.json
{
  'user': 'ellen_greg',
  'action': 'purchase',
  'item_id': '14781239',
}
import json

with open('purchase_14781239.json') as purchase_json:
  purchase_data = json.load(purchase_json)

print(purchase_data['user'])
# Prints 'ellen_greg'
# => We continue by parsing purchase_json using json.load(), creating a Python dictionary out of the file.


# ✅ Writing a JSON file.
turn_to_json = {
  'eventId': 674189,
  'dateTime': '2015-02-12T09:23:17.511Z',
  'chocolate': 'Semi-sweet Dark',
  'isTomatoAFruit': True
}

import json

with open('output.json', 'w') as json_file:
  json.dump(turn_to_json, json_file)
# => use the json.dump() method to write to the file. json.dump() takes two arguments: first the data object, then the file object you want to save.
