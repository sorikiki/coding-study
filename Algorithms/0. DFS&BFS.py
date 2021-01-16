# ✅ 자료구조: 데이터를 표현하고 관리하고 처리하기 위한 구조
# 스택과 큐는 자료구조의 기초 개념
# ◽ 삽입
# ◽ 삭제
# ◽ 오버플로
# ◽ 언더플로

# ❓ Extended Slices
# arr[A:B:C]
# index A부터 index B 까지의 C의 간격으로 배열을 만들어라.

# ✅ 스택: 선입후출 혹은 후입선출 구조
# 별도의 라이브러리가 필요없음
stack = []
stack.append(1)
stack.append(2)
stack.append(3)
stack.pop()
stack.append(4)
stack.append(5)
stack.pop()

print(stack) # [1, 2, 4]
print(stack[::-1]) # [4, 2, 1]

# ✅ 큐: 선입선출 구조
# 큐 구현을 위한 라이브러리 이용해보기
# deque: A list-like sequence optimized for data accesses near its endpoints.
from collections import deque
queue = deque()
queue.append(1)
queue.append(2)
queue.append(3)
queue.popleft()
queue.append(4)
queue.append(5)
print(queue) # deque([2, 3, 4, 5])
queue.reverse()
print(list(queue)) # [5, 4, 3, 2]

# ✅ 재귀함수: 자기 자신을 다시 호출하는 함수
# 내부적으로 스택 자료구조와 동일. 가장 마지막에 호출한 함수가 먼저 수행을 끝내야 그 앞의 함수 호출이 종료되기 때문
def recursive_function(i):
  if i == 3:
    return
  print(i, '번째 재귀 함수에서', i+1, '번째 재귀 함수를 호출')
  recursive_function(i+1)
  print(i, '번째 재귀 함수 종료')

recursive_function(1)
# 1번째 재귀 함수에서 2번째 재귀 함수를 호출
# 2번째 재귀 함수에서 3번째 재귀 함수를 호출
# 2번째 재귀 함수 종료
# 1번째 재귀 함수 종료

def factorial_recursive(n):
  if n <= 1:
    return 1
  return n*factorial_recursive(n-1)

factorial_recursive(3)
# 6

# RecursionError: 무한대로 재귀 호출을 진행한 경우 발생하는 error

# ✅ DFS: 깊이 우선 탐색(특정한 경로로 탐색하다가 특정한 상황에서 최대한 깊숙이 들어가서 노드를 방문한 후, 다시 돌아가 다른 경로로 탐색하는 알고리즘)
# ✔ 노드와 간선의 관계를 표현하는 두 가지 방식
# 1. 인접 행렬 방식
INF = 999999999
graph = [ 
  [0, 7, 5],
  [7, 0, INF],
  [5, INF, 0]
]

print(graph)
# 2. 인접 리스트 방식
graph = [[] for _ in range(3)]

# 노드 0에 연결된 노드 정보 저장
graph[0].append((1, 7))
graph[0].append((2, 5))

# 노드 1에 연결된 노드 정보 저장
graph[1].append((0, 7))

# 노드 2에 연결된 노드 정보 저장
graph[2].append((0, 5))

print(graph)

# => 메모리: 1번 방식에 비해 2번 방식은 메모리를 효율적으로 사용한다. 
# => 속도: 그러나, 이와 같은 속성 때문에 1번에 비해 특정한 두 노드가 연결되어 있는지에 대한 정보를 얻는 속도가 느리다.

# - DFS는 스택 자료구조에 기초한다는 점에서 구현이 간단하다.
# => 실제 구현은 스택을 쓰지 않아도 되며, 재귀함수를 이용했을 때 매우 간결
# - 탐색을 수행함에 있어서 데이터의 개수가 N개인 경우 O(N)의 시간이 소요된다.

def dfs(graph, v, visited): 
  # graph는 노드와 간선의 관계를 나타내는 2차원 리스트, v는 시작노드
  # visited는 각 노드가 방문된 정보를 나타내는 1차원 리스트
  visited[v] = True
  print(v, end=' ') # 탐색 순서에 따라 출력되는 것
  for i in graph[v]:
    if not visited[i]:
      dfs(graph, i, visited)

graph = [
	[],
	[2,3,8],
	[1,7],
	[1,4,5],
	[3,5],
	[3,4],
	[7],
	[2,6,8],
	[1,7],
	]

visited = [False] * 9

dfs(graph, 1, visited)
# 1 2 7 6 8 3 4 5

# ✅ BFS: 너비 우선 탐색(가까운 노드부터 탐색하는 알고리즘)
# '큐'를 이용하는 것, 실제 구현할 때에도 deque 라이브러리를 이용
# N개의 데이터를 처리함에 있어서, O(N)의 시간이 소요됨
# 실제 수행 시간이 DFS보다 좋은 편

from collections import deque

def bfs(graph, start, visited):
  queue = deque([start])
  visited[start] = True
  while queue:
    v = queue.popleft()
    print(v, end=' ')
    for i in graph[v]:
      if not visited[i]:
        queue.append(i)
        visited[i] = True
bfs(graph, 1, visited) # 1 2 3 8 7 4 5 6

# 🔥 정리: DFS는 '스택'을 기초로 '재귀 함수'를 이용, BFS는 '큐'를 기초로 이용

# ✅ 음료수 얼려 먹기
N, M = map(int, input().split())
graph = []
for _ in range(N):
  graph.append(list(map(int, input())))

def dfs2(x, y):
  if x <= -1 or x >= N or y <= -1 or y >= M:
    return False
  if graph[x][y] == 0:
    graph[x][y] = 1
    dfs2(x+1, y)
    dfs2(x, y+1)
    dfs2(x-1, y)
    dfs2(x, y-1)
    return True
  return False

result = 0
for i in range(N):
  for j in range(M):
    if dfs2(i, j) == True:
      result += 1

print(result)

# 미로탈출
from collections import deque

N, M = map(int, input().split())
graph = []
for _ in range(N):
  graph.append(list(map(int, input())))

# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def bfs2(x ,y):
  queue = deque()
  queue.append((x, y))
  while queue:
    x, y = queue.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if nx<0 or nx>=N or ny<0 or ny>=M:
        continue
      if graph[nx][ny] == 0:
        continue
      # 해당 노드를 처음 방문하는 경우만 기록
      if graph[nx][ny] == 1:
        graph[nx][ny] = graph[x][y] + 1
        queue.append((nx, ny))
  return graph[N-1][M-1]

print(bfs2(0, 0))

# ✅ 특정 거리의 도시 찾기(bfs)
from collections import deque

n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)

visited = [0] * (n+1)
def q15(num):
  queue = deque([])
  queue.append(num)
  while queue:
    p = queue.popleft()
    for i in graph[p]:
      if i == 1:
        continue
      if visited[i] == 0:
        queue.append(i)
        visited[i] = visited[p] + 1
  return [_ for _ in range(n+1) if visited[_] == k]

if not q15(x):
  print(-1)
else:
  for _ in q15(x):
    print(_)

# ✅ 연구소
# cf. 재귀함수 알고리즘
# for i in range(2):
#   for j in range(2):
# 스택: (1,1) - (1,2) - (2,1) - return
# (1,1) - (1,2) - (2,2) - return
# (1,1) - (2,1) - (1,2) - return
# (1,1) - (2,1) - (2,2) - return
# (1,1) - (2,2) - (1,2) - return
# (1,1) - (2,2) - (2,1)
# ... 결국 조합이라고는 할 수 없네. 조합은 DFS와 다름

n, m = map(int, input().split())
data = [] # 초기 맵 리스트
temp = [[0]*m for _ in range(n)] # 벽을 설치한 뒤의 맵 리스트

for _ in range(n):
  data.append(list(map(int, input().split())))

# 4가지 이동 방향에 대한 리스트
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

result = 0

# DFS를 이용해 각 바이러스가 사방으로 퍼지도록 하는 메서드
def virus2(x, y):
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    if nx >= 0 and nx <n and ny>=0 and ny<m:
      if temp[nx][ny] == 0:
        temp[nx][ny] = 2
        virus2(nx, ny)

# 현재 맵에서 안전 영역의 크기를 계산하는 메서드
def get_score():
  score = 0
  for i in range(n):
    for j in range(m):
      if temp[i][j] == 0:
        score += 1
  return score

# DFS을 이용해 울타리를 설치하면서, 매번 안전 영역의 크기를 계산
def dfs3(count):
  global result
  if count == 3:
    for i in range(n):
      for j in range(m):
        temp[i][j] = data[i][j]
    # 각 바이러스의 위치에서 전파 진행
    for i in range(n):
      for j in range(m):
        if temp[i][j] == 2:
          virus2(i, j)
    # 안전 영역의 최댓값 계산
    result = max(result, get_score())
    return
  # 빈 공간에 울타리 설치
  for i in range(n):
    for j in range(m):
      if data[i][j] == 0:
        data[i][j] = 1
        count += 1
        dfs3(count)
        data[i][j] = 0
        count -= 1

dfs3(0)
print(result)
# 9

# ✅ 경쟁적 전염
# 큐 사용 하지 않음 = > 치명적인 단점: 시간 초과
n, k = map(int, input().split())
virus = [[0]*(n+1)]
new = [[0]*(n+1) for _ in range(n+1)]
for _ in range(n):
  user = list(map(int, input().split()))
  virus.append([0] + user)
s, x, y = map(int, input().split())

# 상, 우, 하, 좌
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# virus를 퍼뜨리는 함수
def spreadVirus(x, y, t):
  nx = x + dx[t]
  ny = y + dy[t]
  if nx>=1 and nx<=n and ny>=1 and ny<=n:
    if new[nx][ny] == 0:
      new[nx][ny] = virus[x][y]

# s초후에 특정 virus를 찾는 함수
# 1초에 거리1만큼 spread하는 제한 조건 기억
def checkVirus(num):
  while num <= k:
    for i in range(1,n+1):
      for j in range(1, n+1):
        if virus[i][j] == num:
          for t in range(4):
            spreadVirus(i, j, t)
    for i in range(n+1):
      for j in range(n+1):
        if new[i][j] == num and virus[i][j] == 0:
          virus[i][j] = num
    num += 1

for _ in range(s):
  num = 1
  checkVirus(num)
print(virus[x][y])

# ✅ 경쟁적 전염
from collections import deque

queue = deque() 

n, k = map(int, input().split())
virus = [[0]*(n+1)]
for _ in range(n):
  user = list(map(int, input().split()))
  virus.append([0] + user)
s, x, y = map(int, input().split())

time = 0

# 큐를 초기화(행, 열, 초)
for i in range(n+1):
  for j in range(n+1):
    for t in range(k):
      if virus[i][j] == (t+1):
        queue.append((i, j, time))

# 상, 하, 좌, 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def spreadVirus2(row, col, time):
  for i in range(4):
    nx = row + dx[i]
    ny = col + dy[i]
    # 시험관 밖을 벗어나지 않고
    if nx>= 1 and nx<=n and ny>=1 and ny<=n:
      # 방문한 곳이 아니라면
      if virus[nx][ny] == 0:
        queue.append((nx, ny, time))
        virus[nx][ny] = virus[row][col]

for _ in range(s):
  time += 1
  while True:
    # 시간대가 아니라면 종료
    if queue[0][-1] != (time-1):
      break
    if queue:
      z = queue.popleft() # [1,1,0]
      spreadVirus2(z[0], z[1], time)
    else:
      break

print(virus[x][y])

# ✅ 괄호변환
p = input()

def checkNumber(str):
  a = 0
  b = 0
  for i in str:
    if i == "(":
      a += 1
    else:
      b += 1
    if a == b and a >= 1:
      break
  return str[:a+b], str[a+b:]

def checkBalance(u):
  count = 0 # 왼쪽 괄호의 개수
  for i in u:
    if i == "(":
      count += 1
    else:
      if count == 0:
        return False
      count -= 1
  return True

  


def divideString(str):
  result = ''
  if str == '':
    return result
  u, v = checkNumber(str)
  if checkBalance(u):
    result = u + divideString(v)
  else:
    result = ("(" + divideString(v) + ")")
    temp = [")" if i == "(" else "(" for i in u[1:-1] ] 
    result += ''.join(temp)
  return result

print(divideString(p))

# ✅ 연산자 끼워 넣기
n = int(input())
data = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())

max_value = -1e19
min_value = 1e19

def q19(i, now):
  global max_value, min_value, add, sub, mul, div
  if i == n:
    min_value = min(min_value, now)
    max_value = max(max_value, now)
  
  else:
    if add > 0:
      add -= 1
      q19(i+1, now + data[i])
      add += 1
    if sub > 0:
      sub -= 1
      q19(i+1, now - data[i])
      sub += 1
    if mul > 0:
      mul -= 1
      q19(i+1, now * data[i])
      mul += 1
    if div > 0:
      div -= 1
      if now < 0:
        q19(i+1, -(-now // data[i]))
      else:
        q19(i+1, now // data[i])
      div += 1
    
q19(1, data[0])

print(max_value)
print(min_value)

# ➕ 중복순열 라이브러리를 사용한 풀이 
from itertools import product

n = int(input())
data = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())
unfiltered = list(product(['+','-','*','/'], repeat=(n-1)))
filtered = []

# unfiltered: 중복순열 결과
# 중복순열이 
for i in unfiltered:
  if i.count('+')<=add and i.count('-')<=sub and i.count('*')<=mul and i.count('/')<=div:
    filtered.append(i)

min_value = 1e19
max_value = -1e19

for i in filtered:
  now = data[0]
  for j in range(n-1):
    if i[j] == '+':
      now += data[j+1]
    if i[j] == '-':
      now -= data[j+1]
    if i[j] == '*':
      now *= data[j+1]
    if i[j] == '/':
      if now < 0:
        now = -(-now // data[j+1])
      else:
        now //= data[j+1]
  min_value = min(min_value, now)
  max_value = max(max_value, now)

print(max_value)
print(min_value)

# ✅ 감시 피하기
from itertools import combinations

n = int(input())
board = []
teachers = []
space = []

for i in range(n):
  board.append(list(input().split()))
  for j in range(n):
    if board[i][j] == 'T':
      teachers.append((i, j))
    if board[i][j] == 'X':
      space.append((i, j))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 한 선생님의 위치에서 네 가지 방향으로 확인
def broadenArea(obstacles, k, teacher_row, teacher_col):
  while True: 
    # 새로운 위치(행, 열) 변수 초기화
    nx = teacher_row + dx[k]
    ny = teacher_col + dy[k]
    if nx<0 or nx>=n or ny<0 or ny>=n:
      return True
    if obstacles.count((nx, ny)):
      return True
    if board[nx][ny] == 'S':
      return False
    teacher_row = nx
    teacher_col = ny
  
  

# 장애물 설치할 3군데 정하기
def main():
  for i in combinations(space, 3):
    answer = True
    for x, y in teachers:
      for k in range(4):
        if not broadenArea(i, k, x, y):
          answer = False
    # 네 가지 방향 모두 탐색한 후
    if answer:
      print("YES")
      return
  print("NO")
  return
  
main()

# ✅ 인구 이동(DFS: RecursionError)
n, l, r = map(int, input().split())
population = []
for _ in range(n):
  population.append(list(map(int, input().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

answer = 0

while True:
  visited = [[0]*n for _ in range(n)]
  num_group = 1
  for i in range(n):
    for j in range(n):
      block_num = people_num = 0
      group = []
      if q21(i, j):
        num = people_num//block_num
        for x, y in group:
          population[x][y] = num
      else:
        continue
      num_group = max(num_group, len(group))
  if num_group == 1:
    break
  else:
    answer += 1

def q21(x, y):
  global block_num
  global people_num

  if visited[x][y] == 1:
    return False

  visited[x][y] = 1
  block_num += 1
  people_num += population[x][y]
  group.append((x,y))

  for i in range(4):
    nx = x+dx[i]
    ny = y+dy[i]
    if nx>=0 and nx<n and ny>=0 and ny<n:
      result = abs(population[nx][ny] - population[x][y])
    else:
      continue
    if result >= l and result <= r:
      q21(nx, ny)
  return True


print(answer)

# ✅ 인구 이동(BFS: 시간초과)
# from collections import deque

# n, l, r = map(int, input().split())
# population = []
# for _ in range(n):
#   population.append(list(map(int, input().split())))

# answer = 0

# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]

# # BFS 메소드
# def q21(i, j):
#   people_num = population[i][j]
#   group_num = 1
#   group = []

#   queue = deque()
#   queue.append((i, j))
#   group.append((i, j))
#   visited[i][j] = 1

#   while queue:
#     row, col = queue.popleft()

#     for k in range(4):
#       nx = row + dx[k]
#       ny = col + dy[k]
#       if nx >= 0 and nx < n and ny >= 0 and ny < n:
#         if visited[nx][ny] == 0:
#           gap = abs(population[nx][ny] -
#                         population[row][col])
#           if gap >= l and gap <= r:
#             queue.append((nx, ny))
#             visited[nx][ny] = 1
#             people_num += population[nx][ny]
#             group_num += 1
#             group.append((nx, ny))
#   return people_num, group_num, group

# # 인구 수 조정
# def changePopulation(people, block, group):
#   num = people // block
#   for x, y in group:
#     population[x][y] = num


# while True:
#   # 연합인 구성원들을 포함하는 변수 bundle
#   bundle = []
#   # 방문처리 초기화
#   visited = [[0] * n for _ in range(n)]

#   # 연합 형성
#   for i in range(n):
#     for j in range(n):
#       if visited[i][j] == 0:
#         people, block, group = q21(i, j)
#         if block > 1:
#           bundle.append((people, block, group))
  
#   # 연합이 형성되지 않았다면
#   if not bundle:
#     break
#   # 연합이 적어도 하나 형성되었다면
#   for x, y, z in bundle:
#     changePopulation(x, y, z)
#   answer += 1

# print(answer)