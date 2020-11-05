# 상하좌우
N = int(input())
li = list(input().split())
x = 1
y = 1
for i in li:
  if i == 'L' and y != 1:
    y -= 1
  elif i == 'R' and y != 5:
    y += 1
  elif i == 'U' and x != 1:
    x -= 1
  elif i == 'D' and x != 5:
    x += 1
print('({}, {})'.format(x, y))

# 시각(데이터의 총 개수가 86400개이기 때문에 3중 반복문 써도 된다. => 완전 탐색)
n = int(input())

sum = 0
for i in range(0, 60):
  if str(i).count('3') >= 1:
    sum += 1 
sum2 = 0
for j in range(0, n+1):
  if str(j).count('3') >= 1:
    sum2 += 1

result = sum2*60*60 + (n+1)*sum*60 + (n+1)*60*sum - sum2*sum*60 - sum2*60*sum - (n+1)*sum*sum + sum2*sum*sum

print(result)

# 나이트의 위치
col = ['a','b','c','d','e','f','g','h']
pos = input()
x = pos[0] # a
a = 1
for i in col:
  if i == x:
    break
  a += 1
b = int(pos[1]) # 1
count = 0

for _ in [-2, 2]:
  a += _
  if a<1 or a>8:
    continue
  else:
    for _ in [-1, 1]:
      b += _
      if b<1 or b>8:
        continue
      else:
        count += 1

for _ in [-2, 2]:
  b += _
  if b<1 or b>8:
    continue
  else:
    for _ in [-1, 1]:
      a += _
      if a<1 or a>8:
        continue
      else:
        count += 1

print(count)

# 나이트의 위치: 알고리즘 기억해두기! 
pos = input()
x = ord(pos[0]) - ord('a') + 1
y = int(pos[1])

steps = [(-2,-1), (-2,1), (2,1), (2,-1), (-1,-2), (-1,+2), (1,-2), (1,+2)]

result = 0
for step in steps:
  next_x = x + step[0]
  next_y = y + step[1]
  if next_x>=1 and next_x<=8 and next_y>=1 and next_y<=8:
    result += 1

print(result)