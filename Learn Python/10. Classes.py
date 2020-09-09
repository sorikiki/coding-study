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
