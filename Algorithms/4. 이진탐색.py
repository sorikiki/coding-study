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