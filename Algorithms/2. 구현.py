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

# ✅ 럭키 스트레이트
n = input()
l = len(n)//2
s1 = 0
s2 = 0
for i in range(0, l):
  s1 += int(n[i])
  s2 += int(n[i+l])
if s1 == s2:
  print('LUCKY')
else:
  print('READY')

# ✅ 문자열 재정렬(.join()함수와 .isalpha() 함수 활용 ❗❗❗)
data = input()
alpha = []
nsum = 0

for i in data:
  if i.isalpha():
    alpha.append(i)
  else:
    nsum += int(i)

alpha.sort()

if nsum != 0: # 어차피 숫자는 0이상이라서
  alpha.append(str(nsum))

print(''.join(alpha))

# ✅ 문자열 압축
data = input()
length = len(data)
result = []

# 각각의 단위수
for i in range(1, length+1):
  block1 = data[0:i]
  j = 1 # 블록1을 만든 횟수
  l = length - i # 블록1을 만들고 남은 길이
  cnt = 1
  result1 = []
  result2 = []
  while l>0:
    if l<i:
      block2 = data[-1:]
      result2.append(str(1) + data[-l:])
      break
    else:
      block2 = data[j*i:j*i + i]
    if block1 == block2:
      cnt += 1
    else:
      result1.append(str(cnt) + block1)
      cnt = 1
    block1 = block2
    l -= i
    j += 1
  result1.append(str(cnt) + block1)
  t = 0
  for i in result1+result2:
    t += len(i) - i.count('1')
  result.append(t)
print(min(result))

# ✅ 문자열 압축 (답안)
def solution(s):
  answer = len(s)
  # 1개 단위(step)부터 압축 단위를 늘려가며 확인
  for step in range(1, len(s) // 2  + 1):
    compressed = ""
    prev = s[0:step]
    count = 1
    # 단위(step) 크기만큼 증가시키며 이전 문자열과 비교
    for j in range(step, len(s), step):
      if prev == s[j:j+step]:
        count +=1 
    # 다른 문자열이 나왔다면(더 이상 압축 x)
      else:
        compressed += str(count) + prev if count >=2 else prev
        prev = s[j: j + step]
        count = 1
    # 남아 있는 문자열에 대해서 처리
    compressed += str(count) + prev if count >= 2 else prev
    answer = min(answer, len(compressed))
  return answer
  # ❗ 내 코드와 다른 점
  # range()함수에서 세번째 인자를 준것
  # if else 구문의 활용
  # answer의 최소값을 계속해서 갱신해서 return 한 것

# ✅ 좌물쇠와 열쇠
def solution2(key, lock):
  answer = True
  row = []
  col = []
  lock_length = len(lock)
  key_length = len(key)
  cnt_row = 0
  for i in lock:
    cnt_col = 0
    if sum(i) != lock_length:
      row.append(cnt_row)
      for j in i:
        if j == 0:
          col.append(cnt_col)
        cnt_col += 1
    cnt_row += 1
  trans_lock = [[lock[i][j] for j in range(min(col),max(col)+1)] for i in range(min(row), max(row)+1)]

  print(trans_lock)

  for _ in range(4):
    trans_key = []
    # key를 90도 회전한 2차원 배열: trans_key
    for i in range(0, key_length):
      trans_col = []
      for j in range(key_length-1, -1, -1):
        trans_col.append(key[j][i])
      trans_key.append(trans_col)
    print(trans_key)
    # trans_key의 일부와 trans_lock이 상반?
    for i in range(0, len(trans_key[0])-len(trans_lock[0]) + 1):
      for j in range(0, len(trans_key) - len(trans_lock) + 1):
        li = [[trans_key[a][b] for b in range(i, i+len(trans_lock[0]))] for a in range(j, j+len(trans_lock))]
        sum_li = [li[i][j] + trans_lock[i][j] for i in range(0, len(li)) for j in range(0, len(li[0]))]
        print(sum_li)
        if sum_li.count(1) == len(li) * len(li[0]):
          answer= True
          return answer
        else:
          answer= False
  return answer

  # ✅ 기둥과 보 설치
def solution3(n, build_frame):
  answer =[]
  for i in build_frame:
    # 설치
    if i[3]:
      # 기둥 설치
      if i[2] == 0:
        answer.append(install_v(i, answer))
      # 보 설치
      else:
        answer.append(install_h(i, answer))
    # 삭제
    else:
      # 기둥 삭제
      if i[2] == 0:
        if answer.count(remove_v(i,answer)):
          answer.remove(remove_v(i, answer))
      # 보 삭제
      else:
        if answer.count(remove_h(i,answer)):
          answer.remove(remove_h(i, answer))
    answer = trim_result(answer)
  return answer

# 배열을 정리하는 함수
def trim_result(result):
  result = [i[0:3] for i in result if i]
  result.sort()
  return result

# 기둥을 설치하는 함수
def install_v(block, answer):
  # case1. 기둥이 바닥 위에
  if block[1] == 0:
    return block
  # case2. 기둥이 한 쪽 보끝이나 다른 기둥 위에
  else:
    for i in answer:
      if i[0] == block[0]-1 and i[1] == block[1] and i[2] == 1:
        return block
      if i[0] == block[0] and i[1] == block[1] and i[2] == 1:
        return block
      if i[0] == block[0] and i[1] == block[1]-1 and i[2] == 0:
        return block
  return    
      
# 보를 설치하는 함수
def install_h(block, answer):
  # case1. 양 끝점 중 하나라도 기둥이 있을 때
  for i in answer:
    if i[0] == block[0] and i[1] == block[1] -1 and i[2] == 0:
      return block
    if i[0] == block[0]+1 and i[1] == block[1]-1 and i[2] == 0:
      return block
  # case2. 양 side 모두 보일 때
  k = 0
  for i in answer:
    if i[0] == block[0]-1 and i[1] == block[1] and i[2] == 1:
      for j in answer[(k+1):]:
        if j[0] == block[0]+1 and j[1] == block[1] and j[2] == 1:
          return block
    k += 1
  return
  
# 기둥을 삭제하는 함수
def remove_v(block, answer):
  # case1. 아래쪽에 받치는 기둥이 있는 경우
  for i in answer:
    if i[0] == block[0] and i[1] == block[1]-1 and i[2] == 0:
      return
  # case2. 교차점에 있는 보의 반대편이 보와 연결되고 있는 경우
  x2 = [-2, 1, -2, 1]
  x1 = [-1, 0, -1, 0]
  y = [1, 1, 0, 0]
  for j in range(0,4):
    if answer.count([block[0]+x1[j], block[1]+y[j], block[2]+1]) and answer.count([block[0]+x2[j], block[1]+y[j], block[2]+1]):
      return
  return block[0:3]

# 보를 삭제하는 함수
def remove_h(block, answer):
  x2 = [-2, 2]
  x1 = [-1, 1]
  for j in range(0,2):
    if answer.count([block[0]+x1[j], block[1], block[2]]) and answer.count([block[0]+x2[j], block[1], block[2]]):
      return
  return block[0:3]

# 기둥과 보 해설(시간복잡도 O(M**3)으로 해결 가능, 2차원 자료일 경우 다음과 같은 반복문 가능, 원소 IN 배열 구문 활용 가능)
# 현재 설치된 구조물이 '가능한' 구조물인지 확인하는 함수
def possible(answer):
  for x, y, stuff in answer:
    if stuff == 0: # 설치된 것이 '기둥'
      # '바닥 위' 혹은 '보의 한쪽 끝부분 위' 혹은 '다른 기둥 위'라면 정상
      if y == 0 or [x-1, y, 1] in answer or [x, y, 1] in answer or [x, y-1, 0] in answer:
        continue
      return False
    elif stuff == 1: # 설치된 것이 '보'
      # 한쪽 끝부분이 기둥 위 혹은 양쪽 끝부분이 다른 보와 동시에 연결이라면 정상
      if [x, y-1, 0] in answer or [x+1, y-1, 0] in answer or ([x-1, y, 1] in answer [x+1, y, 1] in answer):
        continue
      return False
  return True

def solution4(n, build_frame):
  answer = []
  for frame in build_frame:
    x, y, stuff, operate = frame
    if operate == 0: # 삭제하는 경우
      answer.remove([x, y, stuff])
      if not possible(answer):
        answer.append([x, y, stuff])
    if operate == 1: # 설치하는 경우
      answer.append([x, y, stuff])
      if not possible(answer):
        answer.remove([x, y, stuff])
  return sorted(answer)

# 뱀
n = int(input())
apple = [[0*n for _ in range(n)] for _ in range(n)]
snake = [[1,1]]
k = int(input())
for _ in range(k):
  row, col = map(int, input().split())
  apple[row-1][col-1] = 1
  
turn_sec = []
turn_dir = []
l = int(input())
for _ in range(l):
  s, d = input().split()
  turn_sec.append(int(s))
  turn_dir.append(d)
dr = 0
y = [1, 0, -1, 0]
x = [0, 1, 0, -1]
sec = 0

while True:
  # 1초가 지남
  sec += 1
  # dir에 따라, 뱀의 머리에 따라 다른쪽으로 움직임
  sx = snake[-1][0] + x[dr]
  sy = snake[-1][1] + y[dr]
  # 뱀의 머리가 새롭게 위치할 칸에 자기 몸이나 벽을 만남
  if snake.count([sx, sy]) or sx>n or sx<1 or sy>n or sy<1:
    break
  # 뱀의 머리가 새롭게 위치할 칸에 사과가 있음
  if apple[sx-1][sy-1]:
    snake.append([sx, sy])
  else:
    snake.pop(0)
    snake.append([sx, sy])
  if turn_sec.count(sec):
    idx = turn_sec.index(sec)
    dr = onTurnDirection(turn_dir, idx, dr)
print(sec)

def onTurnDirection(li, idx, dr):
  if li[idx] == 'L':
    dr -= 1
    if dr == -1:
      dr = 3
  else:
    dr += 1
    if dr == 4:
      dr = 0
  return dr

# 뱀 해설
n = int(input())
k = int(input())
data = [[0] * (n+1) for _ in range(n+1)]
info = []

# 맵 정보(사과 있는 곳은 1로 표시)
for _ in range(k):
  a, b = map(int, input().split())
  data[a][b] = 1

# 방향 회전 정보 입력
l = int(input())
for _ in range(l):
  x, c = input().split()
  info.append(int(x), c)

# 동, 서, 남, 북
  dx = [0, 1, 0, -1]
  dy = [1, 0, -1, 0]

def simulate():
  x, y = 1, 1 # 뱀의 머리 위치
  data[x][y] = 2
  direction = 0
  time = 0
  index = 0
  q = [(x, y)]
  while True:
    nx = x + dx[direction]
    ny = y + dy[direction]
    # 맵 범위 안에 있고, 뱀 몸통이 없는 위치라면
    if 1 <= nx and nx <= n and 1 <= ny and ny <= n and data[nx][ny] != 2:
      # 사과가 없다면 이동 후 꼬리 제거
      if data[nx][ny] == 0:
        data[nx][ny] = 2
        q.append((nx,ny))
        px, py = q.pop(0)
        data[px][py] = 0
      # 사과가 있다면 이동 후 꼬리 그대로
      if data[nx][ny] == 1:
        data[nx][ny] = 2
        q.append((nx, ny))
    # 벽이나 몸통에 부딪혔다면,
    else:
      time += 1
      break
    x, y = nx, ny # 다음 위치로 머리를 이동
    time += 1
    if index < l and time == info[index][0]:
      direction = turn(direction, info[index][1])
      index += 1
  return time

def turn(direction, c):
  if c == "L":
    direction = (direction-1)%4
  else:
    direction = (direction+1)%4

  return direction

print(simulate())