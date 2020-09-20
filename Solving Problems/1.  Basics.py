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


# ✅ Day 2 
# ◽ sys.stdin.readline().split()

# ◽ list()

# ◽ EOFError()
while True:
    try:
        a, b = map(int, input().split())
        print(a+b)
    except EOFError:
        break


# ◽ str()

# 1110
num = input()
origin = num
i = 0
while True:
	if len(num) == 1:
		num = '0' + num
	first = int(num[1])
	sum = int(num[0]) + first
	second = str(sum)[-1]
	num = str(first) + second
	i += 1
	if origin == num:
		break
print(i)


# ✅ Day3
'''
# To see the nested lists, you can convert the zip object to a list first:
print(list(names_and_heights)) # [('Jenny', 61), ('Alexus', 70), ('Sam', 67), ('Grace', 65)]
'''

# ◽ zip: 유효성

# 2562
# 1. zip을 이용한 방법
nums = []
for i in range(9):
    num = int(input())
    nums.append(num)
index = list(range(1,10))
pairs = zip(nums, index)
new = list(pairs)
nums.sort()
max = nums[-1]
print(max)
for i, j in new:
    if i == max:
        print(j)

# 2. sorted함수를 이용한 방법
nums = []
for i in range(9):
    num = int(input())
    nums.append(num)
new = sorted(nums)
max = new[-1]
print(max)
idx = nums.index(max) + 1
print(idx)

# ◽ 반복해서 수를 입력받고 싶을 때
A,B,C = [int(input()) for _ in range(3)]

# ◽ sum()

# ◽ 출력형식 지정하는 방법 

# ✅ Day 4
# 4344
num = int(input())
for i in range(num):
    scores = list(map(int, input().split()))
    average = (sum(scores) - scores[0])/scores[0]
    filtered = [i for i in scores[1:] if i>average]
    over_percent = len(filtered)/scores[0]*100
    print(str(format(over_percent,".3f")) + '%')

# 4673: 왜 컴파일 에러야..
def d(n):
    li = list(map(int, str(n)))
    return sum(li)

for i in range(1,10001):
    for j in range(1,i+1):
	    if i == j+d(j):
            break
	    elif j == i:
		    print(i)
	    else:
		    continue