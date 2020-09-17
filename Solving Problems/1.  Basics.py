# ✅ Day 1: 입출력과 사칙연산 + for 반복문에서 range() 함수 사용 
# ◽ input(prompt)
# : If the prompt argument is present, it is written to standard output without a trailing newline. The function then reads a line from input, converts it to a string (stripping a trailing newline), and returns that. 

# ◽ int(x)
# : x is number or string
# => int('100', 8) # 64

# ◽ map(function, object which is iterable)
# ex. a, b = map(int, input().split())

# ◽ floor operator
# : Discard decimal places after division and leave only integers

# ◽ range()
# : The range type represents an immutable sequence of numbers and is commonly used for looping a specific number of times in for loops.
# => The arguments to the range constructor must be integers. If the step argument is omitted, it defaults to 1. If the start argument is omitted, it defaults to 0. If step is zero, ValueError is raised.
# => Often we won’t be iterating through a specific list, we’ll just want to do a certain action n times with range() function!

'''
>>> list(range(10))
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> list(range(1, 11))
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> list(range(0, 30, 5))
[0, 5, 10, 15, 20, 25]
>>> list(range(0, 10, 3))
[0, 3, 6, 9]
>>> list(range(0, -10, -1))
[0, -1, -2, -3, -4, -5, -6, -7, -8, -9]
>>> list(range(0))
[]
>>> list(range(1, 0))
[]
'''

# 2588
a = int(input())
b = input()
b0, b1, b2 = [int(i) for i in b]
print(a*b2)
print(a*b1)
print(a*b0)
print(a*b2+a*b1*10+a*b0*100)

