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
