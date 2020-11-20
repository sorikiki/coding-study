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
# 내부적으로 스택 자료구조와 동일
def recursive_function(i):
  if i == 3:
    return
  print(i, '번째 재귀 함수에서', i+1, '번째 재귀 함수를 호출')
  recursive_function(i+1)
  print(i, '번째 재귀 함수 종료')

def factorial_recursive(n):
  if n <= 1:
    return 1
  return n*factorial_recursive(n-1)

# ✅ DFS: 깊이 우선 탐색(특정한 경로로 탐색하다가 특정한 상황에서 최대한 깊숙이 들어가서 노드를 방문한 후, 다시 돌아가 다른 경로로 탐색하는 알고리즘)
# ✔ 노드와 간선의 관계를 표현하는 두 가지 방식
# 1. 인접 행렬 방식
INF = 999999999
graph = [ 
  [0, 7, 5],
  [7, 0,INF],
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
# => 실제 구현은 재귀함수를 이용했을 때 매우 간결
# - 탐색을 수행함에 있어서 데이터의 개수가 N개인 경우 O(N)의 시간이 소요된다.
