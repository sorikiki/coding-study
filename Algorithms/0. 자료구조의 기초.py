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
