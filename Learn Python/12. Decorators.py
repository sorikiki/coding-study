# ✅ Functions are objects
def added_five(num):
    print(num + 5)

print(added_five(2)) # 7
print(added_five) # <function added_five 'memory address'>
# ❗ Functions are also objects like number, string and list.
# => This means that we can pass them around, store them in variables, return them and use them as parameters and arguments.


# ✅ Functions within functions
def added_six(num):
    def added_two(num):
        return num + 2
    num_added_two = added_two(num) # the 'num' in this line refers to a parameter after 'added_six' function.
    print(num_added_two + 4)

added_six(2) # 8
# added_two(2) => this throws name error!


# ✅ Returning Functions from functions
def get_math_operations(operation):
    def add_nums(n1, n2):
        print(n1 + n2)
    def sub_nums(n1, n2):
        print(n1 - n2)
    if operation == '+':
        return add_nums
    elif operation == '-':
        return sub_nums

add = get_math_operations('+')
sub = get_math_operations('-')

print(add(2, 3)) # 5
print(sub(2, 3)) # -1


# ✅ Decorating a Function
# : it adds additional functions to a original function = this process is like decorating a function.
def title_decorator(print_ones_name):
    def wrapper():
        print('Student:')
        print_ones_name()
    return wrapper

def print_my_name():
    print('dasol')

decorated_function = title_decorator(print_my_name())
decorated_function() # Student: dasol

# ✅ Decorators: Python gives more simple code for decorating a function.
def decorator(print_ones_name):
    def wrapper():
        print('Student:')
        print_ones_name()
    return wrapper

@decorator # It should be right above function declaration.
def print_joes_name():
    print('Joe')

print_joes_name() # 'Student: Joe'

# ✅ Decorators with Parameters
def decorator2(print_ones_info):
    def wrapper(*args):
        print("Student:")
        print_ones_info(*args)
    return wrapper

@decorator2
def print_your_name(name, age):
    print(name + " you are " + str(age))

print_your_name('dasol', 23) # dasol your are 23