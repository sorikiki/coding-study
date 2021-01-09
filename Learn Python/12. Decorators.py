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

from itertools import combinations

n, m = map(int, input().split())
graph = []
for _ in range(n):
  li = list(map(int, input().split()))
  graph.append(li)

# 0인 칸 중 세 개를 뽑아 1로 바꾸기
zero = []
for i in range(n):
  for j in range(m):
    if graph[i][j] == 0:
      zero.append((i,j))

candid = list(combinations(zero, 3))

visited = [[0] * m] * n

def q16(x, y):
  global result
  if x<0 or x>=n or y<0 or y>=m:
    return False
  if not (visited[x][y] and visited[x][y] == 1):
    visited[x][y] = True
    graph[x][y] = 2
    q16(x-1, y)
    q16(x, y-1)
    q16(x+1, y)
    q16(x, y+1)
    return True
  return False
  


for a in candid:
  for b in a:
    graph[b[0]][b[1]] = 1
    for c in range(n):
      for d in range(m):
        if graph[c][d] == 2 and visited[c][d] == False:
          q16(c, d)
    result = [len([p for p in q if p==0]) for q in graph]
    print(sum(result))
