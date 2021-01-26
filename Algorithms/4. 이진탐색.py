# ✅ 순차 탐색
# : 리스트 안에 있는 특정한 데이터를 찾기 위해 앞에서부터 데이터를 하나씩 차례대로 확인하는 방법
# in, count()
# 최악의 경우 시간복잡도는 O(N)
# 데이터가 정렬되어 있지 않아도 상관없음

def sequential_search(n, target, array):
    # 각 원소를 하나씩 확인하며
    for i in range(n):
        # 현재의 원소가 찾고자 하는 원소와 동일한 경우
        if array[i] == target:
            return i+1
print("생성할 원소 개수를 입력한 다음 한 칸 띄고 찾을 문자열을 입력하세요.")
input_data = input().split()
n = int(input_data[0]) # 원소의 개수
target = input_data[1] # 찾고자 하는 문자열

print("앞서 적은 원소 개수만큼 문자열 입력. 구분은 띄어쓰기 한 칸")
array = input().split()

print(sequential_search(n, target, array))

# ✅ 이진 탐색: 반으로 쪼개면서 탐색하기
# : 탐색하고자 하는 범위의 시작점, 끝점, 그리고 중간점 변수 3개를 사용
# 시간복잡도는 O(logN)
# 구현하는 방법은 두 가지 1) 재귀함수 이용 2) 반복문 이용
def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start+end) // 2
    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return binary_search(array, target, start, mid-1)
    else:
        return binary_search(array, target, mid+1, end)

n, target = list(map(int, input().split()))
array = list(map(int, input().split()))

result = binary_search(array, target, 0, n-1)
if result == None:
    print('원소가 존재하지 않습니다.')
else:
    print(f"{result + 1}번째에 원소가 위치합니다")

# 반복문을 이용한 이진탐색 함수
# def binary_searc(array, target, start, end):
#     while start<=end:
#         mid = (start+end) // 2
#         if array[mid] == target:
#             return mid
#         elif array[mid] > target:
#             end = mid-1
#         else:
#             start = mid + 1
#     return None

# 코딩테스트에서 이진 탐색의 실제 구현은 매우 까다롭다.
# 처리해야 할 데이터의 개수나 값이 1000만 단위 이상으로 넘어가거나 탐색 범위의 크기가 1000억 이상이라면 이진 탐색과 같이 O(logN)의 속도를 내야하는 알고리즘을 떠올리자.

# ✅ 이진 탐색 트리: 이진 탐색이 동장할 수 있도록 고안된, 효율적인 탐색이 가능한 자료구조
# 원리
# 1. 부모 노드보다 왼쪽 자식 노드가 작다.
# 2. 부모 노드보다 오른쪽 자식 노드가 크다. 
# 탐색을 위해 루트 노드부터 왼쪽 자식 노드 혹은 오른쪽 자식 노드로 이동하며 반복적으로 방문한다.
# 자식 노드가 없을 때까지 원소를 찾지 못했다면, 이진 탐색 트리에 원소가 없는 것이다.
# cf. 이진 탐색 트리에 데이터를 넣고 빼는 방법은 알고리즘보다는 자료구조에 가까우며, 이진 탐색 트리 자료구조를 구현하도록 요구하는 문제는 출제 빈도가 낮다.

# ✅ 빠르게 입력받기
# 입력 데이터의 개수가 많은 문제에 input() 함수를 사용하면 동작 속도가 느려서 시간 초과로 오답판정을 받을 수 있다. 🤔
# sys 라이브러리의 readline() 함수 사용하기 ✨

import sys
input_data = sys.stdin.readline().rstrip()
print(input_data)

# ✅ bisect 라이브러리
# : 파이썬에서는 이진 탐색을 쉽게 구현할 수 있도록 bisect 라이브러리를 제공한다.
# 정렬된 배열에서 특정한 원소를 찾아야할 때 혹은 값이 특정한 범위에 속하는 원소의 개수를 찾고자 할 때 유용
# 아래 두 함수 모두 시간 복잡도 O(logN)에 동작
# bisect_left(a, x): 정렬된 순서를 유지하면서 리스트 a에 데이터 x를 삽입할 가장 왼쪽 인덱스를 찾는 메서드
# bisect_right(a, x): 정렬된 순서를 유지하도록 리스트 a에 데이터 x를 삽일할 가장 오른쪽 인덱스를 찾는 메서드
from bisect import bisect_left, bisect_right

a = [1, 2, 4, 4, 8]
x = 4
print(bisect_left(a, x)) # 2
print(bisect_right(a,x)) # 4

def count_by_range(a, left_value, right_value):
  right_index = bisect_right(a, right_value)
  left_index = bisect_left(a, left_value)
  return right_index-left_index

a = [1, 2, 3, 3, 3, 4, 4, 8, 9]

print(count_by_range(a, 4, 4)) # 2
print(count_by_range(a, -1, 3)) # 5 => [-1, 3] 범위에 있는 데이터 개수 출력

# ✅ 부품 찾기 예제
n = int(input())
all_product = list(map(int, input().split()))
m = int(input())
ordered_product = list(map(int, input().split()))

all_product.sort() # nlogn의 시간복잡도

# 아래의 이진탐색의 시간복잡도는 m*logn

def findNumber(target):
  start = 0
  end = n-1
  
  while start <= end:
    # 중간점 인덱스
    mid = (start + end) // 2
    if all_product[mid] == target:
      return "yes"
    elif all_product[mid] > target:
      end = mid-1
    else:
      start = mid+1
  return "no"

for target in ordered_product:
  print(findNumber(target), end=" ")
# 최종적인 시간복잡도는 O((n+m) * logn)

# ◽ 계수 정렬 이용하기
n = int(input())
all_product = [0] * 100001
product = list(map(int, input().split()))
for i in product:
  all_product[i] = 1
m = int(input())
ordered_product = list(map(int, input().split()))

for target in ordered_product:
  if all_product[target] == 1:
    print("yes", end=" ")
  else:
    print("no", end=" ") 
# 시간복잡도는 O(n + 100001)

# ◽ 집합 자료형 이용
n = int(input())
all_product = set(map(int, input().split()))
m = int(input())
ordered_product = list(map(int, input().split()))

for target in ordered_product:
  if target in all_product:
    print("yes", end=" ")
  else:
    print("no", end=" ") 

# ✅ 떡볶이 떡 만들기
n, m = map(int, input().split())
temp = list(map(int, input().split()))

def sliceCake(start, end):
  while True:
    # 중간 인덱스와 잘린 떡 길이 구하기
    mid = (start+end)// 2
    h = 0
    for i in temp:
      if i>mid:
        h += (i-mid)
    # 반복문 중단 조건
    if h == m or end-start == 1:
      return mid
    elif h > m:
      start = mid
    else:
      end = mid


print(sliceCake(0, max(temp)))

# ◽ 중간값(mid)과는 별개로 새로운 변수 만들어 답안 작성
n, m = list(map(int, input().split()))
array = list(map(int, input().split()))

start = 0
end = max(array)

result = 0
while start <= end:
  total = 0
  mid = (start + end) // 2
  for x in array:
    if x > mid:
      total += x - mid
  # 떡의 양이 부족한 경우 더 많이 자르기
  if total < m:
    end = mid-1
  # 떡의 양이 충분한 경우 덜 자르기
  else:
    result = mid # 최대한 덜 잘랐을 때가 정답이므로, 여기에서 result를 기록
    start = mid + 1
# cf. parametric search: 원하는 조건을 만족하는 가장 큰 값을 찾는 최적화 문제를, 이진 탐색을 이용하여 결정 문제(예 혹은 아니오로 답하는 문제)로 바꾸어 해결

# ✅ 정렬된 배열에서 특정 수의 개수 구하기
# ◽ 이진 탐색 직접 구현
n, x = map(int, input().split())
elements = list(map(int, input().split()))

def count_by_value(array, x):

  first= findFirst(array, x)

  if first == None:
    return -1
  
  last = findLast(array, x)
  
  return last-first+1

def findLast(array, x):
  start = 0
  end = n-1
  answer = None
  while start <= end:
    mid = (start+end)//2
    if array[mid] <= x:
      if array[mid] == x:
        answer = mid
      start = mid + 1
    else:
      end = mid-1
  return answer


def findFirst(array, x):
  start = 0
  end = n-1
  answer = None
  while start <= end:
    mid = (start+end)//2
    if array[mid] >= x:
      if array[mid] == x:
        answer = mid
      end = mid-1
    else:
      start = mid+1
  return answer

print(count_by_value(elements, x))

# ◽ bisect 라이브러리 이용
from bisect import bisect_left, bisect_right

n, x = map(int, input().split())
elements = list(map(int, input().split()))

left_index = bisect_left(elements, x)
right_index = bisect_right(elements, x)

answer = right_index-left_index
result = answer if answer != 0 else -1

print(result)

# ✅ 고정점 찾기
def q28(array, start, end):
  if start > end:
    return None
  mid = (start+end) // 2
  if array[mid] == mid:
    return mid
  elif array[mid] > mid:
    return q28(array, start, mid-1)
  else:
    return q28(array, mid+1, end)

n = int(input())
points = list(map(int, input().split()))

index = q28(points, 0, n-1)

if index == None:
  print(-1)
else: 
  print(index)

# ✅ 공유기 설치 
n, c = map(int, input().split())
house = []
for _ in range(n):
  house.append(int(input()))
house.sort()
# gap의 범위에 대한 시작점과 끝점
start = house[1] - house[0] # 1
end = house[-1] - house[0] # 8

result = 0

while start<=end:
  mid = (start + end)//2
  value = house[0]
  count = 1
  for i in range(1,n):
    if house[i] >= value + mid:
      count += 1
      value = house[i]
  if count >= c:
    start = mid + 1
    result = mid
  else:
    end = mid - 1

print(result)