# ✅ 선택 정렬
# 데이터가 무작위로 여러 개 있을 때, 이 중에서 가장 작은 데이터를 선택해 맨 앞에 있는 데이터와 바꾸고,
# 그다음 작은 데이터를 선택해 앞에서 두 번째 데이터와 바꾸는 과정을 반복...
# ✨ 스와프(swap): 특정한 리스트가 주어졌을 때 두 변수의 위치를 변경하는 작업
# 시간복잡도: O(N**2) => N이 10000개 이상일 경우 정렬 속도가 급격히 느려진다는 단점
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(array)):
    min_index = i # 가장 작은 원소의 인덱스
    for j in range(i+1, len(array)):
        if array[min_index] > array[j]:
            min_index = j
    array[i], array[min_index] = array[min_index], array[i] # 스와프

print(array)

# ✅ 삽입 정렬
# 데이터를 하나씩 확인하며, 각 데이터를 적절한 위치에 삽입한다!
# 선택 정렬에 비해 구현이 어렵지만, 실행 시간 측면에서 효율적
# 특히 삽입 정렬은 필요할 때만 위치를 바꾸므로 '데이터가 거의 정렬되어 있을 때 효율적'
# 삽입 정렬은 특정한 데이터가 적절한 위치에 들어가기 이전에, 그 앞까지의 데이터는 이미 정렬되어 있다고 가정
# => 즉, 첫번재 데이터는 그 자체로 정렬되어 있다고 가정하기 때문에, 삽입 정렬은 두번째 데이터부터 시작
for i in range(1,len(array)):
    for j in range(i, 0, -1): # j 변수가 i부터 1까지 1씩 감소함. 
        if array[j] < array[j-1]:
            array[j], array[j-1] = array[j-1], array[j]
        else: 
            break

# ✅ 퀵 정렬: 이름부터가 '빠른 정렬 알고리즘'일 정도. 정렬 라이브러리의 근간이 되는 알고리즘
# 기준 데이터를 설정하고 그 기준보다 큰 데이터와 작은 데이터의 위치를 바꾸면 어떨까? 
# 시간복잡도: NlogN => 데이터의 개수가 많을수록 퀵 정렬은 앞서 다루었던 선택 정렬, 삽입 정렬에 비해 압도적으로 빠르게 동작한다.
# 다만, 최악의 경우의 시간복잡도는 O(N)이다. 데이터가 무작위로 입력되는 경우, 퀵정렬은 빠르게 동작할 확률이 높으나, 이미 데이터가 정렬되어 있는 경우에는 매우 느리게 동작

# 1. 널리 사용되는 가장 직관적인 형태의 퀵 정렬 소스 코드
array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array, start, end):
    pivot = start # 피벗은 첫번째 원소
    left = start + 1
    right = end
    while left <= right:
        # 피벗보다 큰 데이터를 찾을 때까지 반복(피벗보다 큰 데이터가 없을 수 있으니)
        while left <= end and array[left] <= array[pivot]:
            left += 1
        # 피벗보다 작은 데이터를 찾을 때까지 반복
        while right >= start and array[right] >= array[pivot]:
            right -= 1
        if left > right: # 엇갈렸다면 작은 데이터와 피벗을 교체
            array[right], array[pivot] = array[pivot], array[right]
        else:
            array[left], array[right] = array[right], array[left]
    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행
    quick_sort(array, start, right-1)
    quick_sort(array, right+1, end)

quick_sort(array, 0, len(array) - 1)
print(array)

# 2. 파이썬의 장점을 살린 퀵 정렬 소스코드
def quick_sort(array):
    if len(array) <= 1:
        return array
    
    pivot = array[0]
    tail = array[1:]

    left_side = [x for x in tail if x <= pivot] 
    right_side = [x for x in tail if x > pivot]

    return quick_sort(left_side) + [pivot] + quick_sort(right_side)

print(quick_sort(array))

# ✅ 계수 정렬: 특정한 조겁이 부합할 때만 사용할 수 있지만 매우 빠른 정렬 알고리즘
# 가장 큰 데이터와 가장 작은 데이터의 차이가 1000000을 넘지 않을 때 효과적으로 사용 가능하며 데이터가 0또는 양의 정수여야 함.
# 앞 세 정렬방식의 비교가 아님. 별도의 리스트를 선언하고 그 정렬에 대한 정보를 담음.
# 시간 복잡도: O(N+K) => N은 데이터의 개수, K는 데이터 중 최댓값의 크기 
# 공간 복잡도: 때로는 심각한 비효율성을 초래(데이터가 0과 999,999만 존재하는 경우). 동일한 값을 가지는 데이터가 여러 개 등장할 때 적합
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
count = [0] * (max(array) + 1)

for i in range(len(array)):
    count[array[i]] += 1

for i in range(len(count)):
    for j in range(count[i]):
        print(i, end= ' ')

# ✅ 파이썬의 정렬 라이브러리
# ✔ sorted(), sort(): key 매개변수를 입력으로 받을 수 있다. key 값으로는 하나의 함수가 들어가야 하며 이는 정렬의 기준이 된다.
array = [('바나나', 2), ('사과', 5), ('당근', 3)]

def setting(data):
    return data[1]
result = sorted(array, key=setting) # 리스트의 원소의 두번째 인자에 따라 (오름차순으로) 정렬됨.
# ✔ 정렬 라이브러리의 시간 복잡도
# : 항상 최악의 경우에도 시간 복잡도 O(NlogN)을 보장.
# => 문제에서 별도의 요구가 없다면 단순히 정렬해야 하는 상황에서는 기본 정렬 라이브러리를 사용하고
# => 데이터의 범위가 한정되어 있으며 더 빠르게 동작해야 할 때는 계수 정렬을 사용하자.

# ✅ 예제문제
# ◽ 위에서 아래로
n = int(input())
data = []
for _ in range(n):
  data.append(int(input()))
data.sort(reverse=True)

for i in data:
  print(i, end= ' ')

# ◽ 성적이 낮은 순서로 학생 출력하기
# ✔ 서로 다른 유형의 데이터(이름, 점수)가 들어있는 container로서의 자료형은 튜플로!
# ✔ lambda 표현식 익히기
n = int(input())
data = []

for _ in range(n):
  input_data = input().split()
  data.append((input_data[0], int(input_data[1])))

data = sorted(data, key=lambda student: student[1])

for i in data:
  print(i[0], end=' ')

# ◽ 두 배열의 원소 교체
n, k = map(int, input().split())
array_a = list(map(int, input().split()))
array_b = list(map(int, input().split()))

array_a.sort()
array_b.sort(reverse=True)

for i in range(3):
  if array_a[i] < array_b[i]:
    array_a[i], array_b[i] = array_b[i], array_a[i]

print(sum(array_a))

# ✅ 국영수
n = int(input())
data = []
for _ in range(n):
    data.append(input().split())


data.sort(key=lambda info: (-int(info[1]), int(info[2]), (-int(info[3]), info[0])))

for i in data:
    print(i[0])

# ✅ 안테나
n = int(input())
house = list(map(int, input().split()))
house_sorted = sorted(house)
if n % 2 == 0:
    print(house_sorted[n//2-1])
else:
    print(house_sorted[n//2])

# if 와 else로 나눠쓸 필요도 없이, 그저 print(house_sorted[n//2]) 하면 더 concise해짐.

# ✅ 카드 정렬하기: ZeroDivisionError 처리할 것
def solution(N, stages):
    total = len(stages)
    answer = []

    for i in range(1, N+1):
        if total == 0:
          answer.append((i, 0))
          continue
        num = stages.count(i) # i번재 스테이지에서 실패한 이용자 수
        answer.append((i, num/total)) # 스테이지 번호와 실패율을 튜플로 묶어 리스트에 저장
        total -= num
        
        
    answer.sort(reverse=True, key=lambda x: x[1])
    answer = [x for x, y in answer]
    return answer