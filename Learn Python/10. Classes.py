# ✅ Types
# : We can check the type of a Python variable using the type() function.


# ✅ Class
# : A class is a template for a data type. 
class CoolClass:
    pass

# ◽ Instantiation
# : A class must be instantiated. In other words, we must create an instance of the class, in order to breathe life into the schematic.
# => Instantiating a class looks a lot like calling a function.
cool_instance = CoolClass()
# => A class instance is also called an 'object'. => Object Oriented Programming 
# => Instantiation takes a class and turns it into an object, the type() function does the opposite of that.
print(type(cool_instance))
# prints "<class '__main__.CoolClass'>"
# => In Python __main__ means “this current file that we’re running”

# ✅ Class Variables
# : A class variable is a variable that’s the same for every instance of the class.
# => You can define a class variable by including it in the indented part of your class definition, and you can access all of an object’s class variables with object.variable syntax.
class Musician:
  title = "Rockstar"

drummer = Musician()
print(drummer.title)
# prints "Rockstar"

# ✅ Class Methods (none argument)
# : Methods are functions that are defined as part of a class. 

# - None arguments
# => The first argument in a method is always the object that is calling the method. 
# => Convention recommends that we name this first argument self.
# => Methods always have at least this one argument.
class Dog:
  dog_time_dilation = 7

  def time_explanation(self):
    print("Dogs experience {} years for every 1 human year.".format(self.dog_time_dilation))

pipi_pitbull = Dog()
pipi_pitbull.time_explanation()
# Prints "Dogs experience 7 years for every 1 human year."
# => Notice we didn’t pass any arguments when we called .time_explanation(), but were able to refer to self in the function body.


# ✅ Class Methods (with arguments)
class DistanceConverter:
  kms_in_a_mile = 1.609
  def how_many_kms(self, miles):
    return miles * self.kms_in_a_mile

converter = DistanceConverter()
kms_in_5_miles = converter.how_many_kms(5)
print(kms_in_5_miles)
# prints "8.045"
# => Notice again that even though how_many_kms takes two arguments in its definition, we only pass miles, because self is implicitly passed (and refers to the object converter).


# ✅ Constructors (= dunder methods)
# They are different from other methods and so-named because they have two underscores (double-underscore abbreviated to “dunder”) on either side of them.

# ◽ __init__
# : This method is used to initialize a newly created object.
# => The word “constructor” is used to describe similar features in other object-oriented programming languages but programmers who refer to a constructor in Python are usually talking about the __init__ method.
class Circle:
  pi = 3.14
  
  # Add constructor here:
  def __init__(self, diameter):
    print("New circle with diameter: {diameter}".format(diameter=diameter))
    
teaching_table = Circle(36)


# ✅ Instance Variables
# : The data held by an object is referred to as an instance variable. Instance variables aren’t shared by all instances of a class — they are variables that are specific to the object they are attached to.
class Store:
  pass

alternative_rocks = Store()
isabelles_ices = Store()

alternative_rocks.store_name = "Alternative Rocks"

isabelles_ices.store_name = "Isabelle's Ices"
# ❗ If we attempt to access an attribute that is neither a class variable nor an instance variable of the object Python will throw an AttributeError.

# => What if we aren’t sure if an object has an attribute or not? hasattr() will return True if an object has a given attribute and False otherwise. 
# =>  If we want to get the actual value of the attribute, getattr() is a Python function that will return the value of a given object and attribute.
'''
The syntax and parameters for these functions look like this:

✔ hasattr(object, “attribute”) has two parameters:

object : the object we are testing to see if it has a certain attribute
attribute : name of attribute we want to see if it exists

✔ getattr(object, “attribute”, default) has three parameters (one of which is optional):

object : the object whose attribute we want to evaluate
attribute : name of attribute we want to evaluate
default : the value that is returned if the attribute does not exist (note: this parameter is optional)
'''

can_we_count_it = [{'s': False}, "sassafrass", 18, ["a", "c", "s", "d", "s"]]

for item in can_we_count_it:
  if hasattr(item, 'count'):
    print(str(type(item)) + ' has the count attribute!')
  else: 
    print(str(type(item)) + " does not have the count attribute :(")
'''
<class 'dict'> does not have the count attribute :(
<class 'str'> has the count attribute!
<class 'int'> does not have the count attribute :(
<class 'list'> has the count attribute!
'''


# ✅ Self
# ❓ Since we can already use dictionaries to store key-value pairs, using objects for that purpose is not really useful.
class SearchEngineEntry:
  secure_prefix = "https://"
  def __init__(self, url):
    self.url = url

  def secure(self):
    return "{prefix}{site}".format(prefix=self.secure_prefix, site=self.url)

codecademy = SearchEngineEntry("www.codecademy.com")
wikipedia = SearchEngineEntry("www.wikipedia.org")

print(codecademy.secure())
# prints "https://www.codecademy.com"

print(wikipedia.secure())
# prints "https://www.wikipedia.org"
# => We access both the class variable self.secure_prefix and the instance variable self.url to return a secure URL.
# => 💫 This is the strength of writing object-oriented programs. We can write our classes to structure the data that we need and write methods that will interact with that data in a meaningful way.


# ✅ Everything is an Object

# - dir()
# : We can use the dir() function to investigate an object’s attributes at runtime. dir() is short for directory and offers an organized presentation of object attributes.
class FakeDict:
  pass

fake_dict = FakeDict()
fake_dict.attribute = "Cool"

dir(fake_dict)
# Prints ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'attribute']
# => That’s certainly a lot more attributes than we defined! Python automatically adds a number of attributes to all objects that get created. 
# => These internal attributes are usually indicated by double-underscores. But sure enough, attribute is in that list.

# - Do you remember being able to use type() on Python’s native data types? 
# => ❗❗ This is because they are also objects in Python.
# => cf. type() returns the actual class an object is an implementation of. Although calling type with a class returns a type object.
# => Their classes are int, float, str, list, and dict. These Python classes have special syntax for their instantiation, 1, 1.0, "hello", [], and {} specifically.
# => But these instances are still full-blown objects to Python.


# ✅ String Representation
# => Unfortunately, when we print out an object we get a default representation that seems fairly useless.
# => This default string representation gives us some information, like where the class is defined and our computer’s memory address where this object is stored, but is usually not useful information to have when we are trying to debug our code.

# ◽ __repr__
# : This is a method we can use to tell Python what we want the string representation of the class to be.
# =>  __repr__ can only have one parameter, self, and must return a string.
class Employee():
  def __init__(self, name):
    self.name = name

  def __repr__(self):
    return self.name

argus = Employee("Argus Filch")
print(argus)
# prints "Argus Filch"

