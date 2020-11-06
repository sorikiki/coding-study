# ✅ 상하좌우
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

# ✅ 시각(데이터의 총 개수가 86400개이기 때문에 3중 반복문 써도 된다. => 완전 탐색)
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

# ✅ 나이트의 위치
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

# ✅ 나이트의 위치: 알고리즘 기억해두기! 
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

# ✅ 게임 개발
n, m = map(int, input().split())
d = [[0] *m for _ in range(n)]
x, y, direction = map(int, input().split())
d[x][y] = 1

array = []
for i in range(n):
  array.append(list(map(int, input().split())))
    
# 북, 동, 남, 서 방향 정의
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 왼쪽으로 회전
def turn_left():
  global direction
  direction -= 1
  if direction == -1:
    direction = 3


# 시뮬레이션 시작
count = 1
turn_time = 0
while True:
  turn_left()
  nx = x + dx[direction]
  ny = y + dy[direction]
  # 회전한 이후 정면에 가보지 않은 칸이 존재
  if d[nx][ny] == 0 and array[nx][ny] == 0:
    d[nx][ny] = 1
    x = nx
    y = ny
    count += 1
    turn_time = 0
    continue
  # 회전한 이후 정면에 가보지 않은 칸이 x거나 바다일 때
  else:
    turn_time += 1
  # 네 방향 모두 갈 수 없는 경우
  # 바라보고 있는 방향을 유지한 채로 뒤로
  if turn_time == 4:
    nx = x - dx[direction]
    ny = y - dy[direction]
    # 뒤로 갈 수 있다면 이동하기
    if array[nx][ny] == 0:
      x = nx
      y = ny
    # 뒤가 바다로 막혀있는 경우
    else:
      break
    turn_time = 0

    
print(count)