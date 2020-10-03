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

# 4673
# ❗ indentation 혼용 no(space+tab)

# ◽ set()
#  https://wikidocs.net/16044

# ✔ what is 'set'?
# - mutable object
# - cannot contain mutable elements(list, dictionary, set)
# - unordered (= we cannot access to it by indexing.)

# ✔ how to create?
# - The set uses the same brackets as the disk type, so it cannot be created with brackets alone.
'''
>>> s = {}
>>> type(s)
<class 'dict'>
>>> s = set()
>>> type(s)
<class 'set'>
>>> s
set()
'''
# - When you insert an iterable object in the set constructor, it converts and creates a set.
# - Of course, you can put the value in brackets without the set constructor
'''
>>> s = set([1,3,5,7])
>>> s
{1, 3, 5, 7}
>>> p = {1, 3, 5, 7}
>>> p
{1, 3, 5, 7}
'''

# ✔ Remove duplicate elements
'''
>>> s = {1, 5, 1, 1, 1, 3, 7}
>>> s
{1, 3, 5, 7}
'''

# ✔ in (same with other collection types)
'''
>>> 2 in r
True
>>> 3 in r
False
>>> 3 not in r
True
'''

# ✔ add & update (remove, discard is also available.)
k = {1, 2, 3}
k.add(4) # only add one element
k.update([4,5,6]) # add several elements => {1, 2, 3, 4, 5, 6}

a = {1, 2, 3}
a.update([1, 2, 4]) # { 1, 2, 3, 4}

# ✔ copy

# ✔ operators: |(합집합), -(차집합), ^(대칭차집합)

# ✨ Let's use the feature of the set to eliminate redundant elements.
setA = {i for i in range(1, 10001)}
setB = set()
for i in range(1, 10001):
    for j in str(i):
        i += int(j)
    setB.add(i)

setA = sorted(setA-setB)
for i in setA:
    print(i)


# ✅ Day 5
# ◽ CHARACTER => ASCII 
# - 문자 -> 아스키코드 : ord("문자")
# - 아스키코드 -> 문자 : chr("아스키코드")

# ◽ max()

# 1157
s = list(input().upper())
cnt = []
for i in range(ord('A'),ord('Z')+1):
    cnt.append(s.count(chr(i)))
max_cnt = max(cnt)
if cnt.count(max_cnt) > 1 :
    print("?")
else:
    print(chr(ord('A') + cnt.index(max_cnt)))


# ✅ Day6
# ◽ reverse(), reversed()
# 1. reverse() return none, but reversed() return reversed list.
# => Their relationship is similar to sort() and sorted()
# 2. reverse() is a method only to list, but reversed() is a method to list and string.
s = 'abcde'
s_list = list(s)  # reverse 함수를 사용하기 위해 문자열을 list로 치환
s_list.reverse()  # reverse 함수를 사용해 문자열 리스트를 거꾸로 뒤집음

print(''.join(s_list))  # 거꾸로 뒤집어진 리스트를 연결해서 출력

s = 'abcde'
print(''.join(reversed(s)))  # 'edcba'

# ◽ Easiest way to reverse string
s = 'abcde'
print(s[::-1])  # 'edcba'

s = 'abcde'
print(s[3:0:-1])  # dcb

# 2908
li = list(input().split())
for i in [-1,-2,-3]:
    if li[0][i] == li[1][i]:
        continue
    elif li[0][i] > li[1][i]:
        print(li[0][::-1])
        break
    else:
        print(li[1][::-1])
        break

# ◽ use 'in' operator to check some string into full string.
# 2941
chr = input()
cnt = len(chr)
cr = ['c=','c-','dz=','d-','lj','nj','s=','z=']
for i in cr:
    cnt -= chr.count(i)
print(cnt)


# ✅ Day7
# ◽ UnbouncedLocalError => use keyword 'global' ✨
x = 10
def foo():
    print(x)
    # x += 1 => error
# : This is because when you make an assignment to a variable in a scope, that variable becomes local to that scope and shadows any similarly named variable in the outer scope.
# => Since the last statement in foo assigns a new value to x, the compiler recognizes it as a local variable. Consequently when the earlier print(x) attempts to print the uninitialized local variable and an error results.
# => In the example above you can access the outer scope variable by declaring it global 😊:
x = 10
def foobar():
    global x
    print(x)
    x += 1
# => This explicit declaration is required in order to remind you that you are actually modifying the value of the variable in the outer scope.

# + You can do a similar thing in a nested scope using the nonlocal keyword:
def foos():
    x = 10
    def bar():
        nonlocal x
        print(x)
        x += 1
    bar()
    print(x)
foos()
# ◽ global : This keyword is useful when we need to assign any value to global object inside any function.
# ◽ nonlocal : This keyword is useful when we need to assign any value to nested scope variable.

# 1712
# 😡 fail code => exceed time! 
A, B, C = map(int, input().split())
n = 1
def printn(x, y, z):
    global n
    if z-y <= 0:
        print(-1)
    else:
        while x/(z-y)>=n:
            n += 1
        print(n)
printn(A, B, C)

# 😀 success code
import math
A, B, C = map(int, input().split())
def print_n(x, y, z):
    if z-y <= 0:
        print(-1)
    else:
        h = x/(z-y)
        if h % 1 == 0:
            print (int(h+1))
        else:
            print(int(math.ceil(h)))
print_n(A, B, C)

# 2839
n = int(input())
p5 = n//5
k = n%5
p3 = 0
def pp(n):
    global p5, k, p3
    while p5>=0:
        if k % 3 == 0:
            p3 = k//3
            print (p3+p5)
            break
        else:
            if p5 == 0:
                print(-1)
                break
            p5 -= 1
            k = n-5*p5
pp(n)


# ✅ let's solve math problems 

# 1193
# 😡 fail code => 시간 초과 에러(행과 열을 모두 rotate한다.)
n = int(input())
i = 1
finish = False
while True:
    k = 0
    while k<i:
        k += 1
        if int(i*(i-1)/2+k) == n:
            finish = True
            break
    if finish == True:
        if i%2 == 0:
            a = k
            b = i-k+1
        else:
            a = i-k+1
            b = k
        print(str(a)+'/'+str(b))
        break
    i += 1

# 😊 success code (행만 rotate한다.)
X = int(input())
stage, key_X = 1, 1
while stage + key_X <= X:
    key_X += stage
    stage += 1
step = X-key_X
x, y = stage-step, step+1
if stage%2 == 0:
    print('{}/{}'.format(y,x))
else:
    print('{}/{}'.format(x,y))

# 2292
X = int(input())
if X == 1:
    print(1)
else:
    sum, key_X, i = 2, 2, 6
    while key_X + i <= X:
        key_X += i
        i += 6
        sum += 1
    print(sum)

# 2869
import math
A, B, V= map(int,input().split())
print(math.ceil((V-A)/(A-B)+1))

# 10250
T = int(input())
for i in range(T):
    H, W, N = map(int, input().split())
    n = 0
    finish = False
    while True:
    	if finish == True:
    		print(int(str(j)+format(i,"02")))
    		break
    	i = 0
    	for _ in range(W):
    		if finish == True:
    			break
    		i += 1
    		j = 0
    		for _ in range(H):
    			j += 1
    			n += 1
    			if n == N:
    				finish = True
    				break

# 2775
T = int(input())
for _ in range(T):
    li = list(range(1, 15))
    k, n = [int(input()) for _ in range(2)]
    for _ in range(k):
        i = 1
        for _ in range(n-1):
            li[i] = li[i-1] + li[i]
            i += 1
    print(li[n-1])

# 1011
import math
T = int(input())
for _ in range(T):
    a, b = map(int, input().split())
    n = b-a
    rootn = n**(1/2)
    if rootn % 1 == 0:
        print(2*int(rootn)-1)
    else:
        k = math.floor(rootn)
        if n-k**2 < (k+1)**2-n:
            print(2*k)
        else:
            print(2*k+1)

# 1978
n = int(input())
li = list(map(int, input().split()))
sosu = []
for i in li:
    k, sum = 0, 0
    for j in range(i):
        k += 1
        if i % k == 0:
            sum += 1
    if sum == 2:
        sosu.append(i)
print(len(sosu))


# 2581 review 필요
M,N = [int(input()) for i in range(2)]
s = set()
if M == 1 or M == 2:
	s = set(range(3, N+1, 2))
	if N>=2:
		s.add(2)
else:
	if M % 2 == 0:
		M += 1
	s = set(range(M, N+1, 2))
p = 3
while p**2 <= N:
	k = set()
	for i in s:
		if i % p == 0:
			k.add(i)
	s = s-k
	if p in list(range(M, N+1)):
		li = []
		for _ in list(range(1, p+1)):
			if p % _ == 0:
				li.append(_)
		if len(li) == 2:
			s = s | {p}
	p += 1
if len(s) == 0:
	print(-1)
else:
	print(sum(s))
	print(min(s))


# 1929 시간초과 에러
M, N = map(int, input().split())
s = set()
if M == 1 or M == 2:
	s = set(range(3, N+1, 2))
	if N>=2:
		s.add(2)
else:
	if M % 2 == 0:
		M += 1
	s = set(range(M, N+1, 2))
p= 3
while p**2 <= N:
	k = set()
	for i in s:
		if i % p == 0:
			k.add(i)
	s = s-k
	if p in list(range(M, N+1)):
		li = []
		for _ in list(range(1, p+1)):
			if p % _ == 0:
				li.append(_)
		if len(li) == 2:
			s = s | {p}
	p += 1
for _ in sorted(s):
	print(_)

# 1929 
M, N  = map(int, input().split())

num_range = [True] * (N+1)
num_range[0] = False
num_range[1] = False

i = 2
while i**2<=N:
    if num_range[i] == True:
        j = i*i
        while j<=N:
            num_range[j] = False
            j += i
    i += 1
for k in range(M, N+1):
    if num_range[k]:
        print(k)

# 4948
while True:
	n = int(input())
	if n == 0:
		break
	range = [True] * (2*n + 1)
	range[0] = False
	range[1] = False
	p = 2
	while p ** 2 <= 2*n:
		if range[p] == True:
			j = p * p
			while j <= 2*n:
				range[j] = False
				j += p
		p += 1
	li = sum(range[n+1:2*n+1])
	print(li)

# 9020
t = int(input())
for _ in range(t):
    n = int(input())
    range = [True] * (n+1)
    range[0] = False
    range[1] = False
    p = 2
    while p**2 <= n:
        if range[p] == True:
            j = p*p
            while j<=n:
                range[j] = False
                j += p
        p += 1
    k = n//2
    while k>=2:
        if range[k] == True and range[n-k] == True:
            print(k, n-k)
            break
        k -= 1