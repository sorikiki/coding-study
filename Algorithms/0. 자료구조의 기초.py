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