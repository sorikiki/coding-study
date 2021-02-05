# ✅ 다이나믹 프로그래밍
# = 동적 계획법
# 메모리 공간을 약간 더 사용하여 연산 속도를 비약적으로 증가시킬 수 있는 방법

# 다음 조건을 만족할 때 다이나믹 프로그래밍을 사용할 수 있다.
# 1. 큰 문제를 작은 문제로 나눌 수 있다. 분할 정복 알고리즘(ex. 퀵 정렬)과 유사하나, 다이나믹 프로그래밍은 퀵 정렬과 달리 한 번 해결한 문제를 다시금 해결한다는 특징이 있음
# 2. 작은 문제에서 구한 정답은 그것을 포함하는 큰 문제에서도 동일하다.

# WAY 1: 재귀함수 (탑다운 방식: 큰 문제 해결을 위해 작은 문제 해결)
# ◽ Code 1: 피보나치 수열의 점화식을 재귀함수를 이용해 표현
def fibo(x):
    if x == 1 or x == 2:
        return 1
    return fibo(x - 1) + fibo(x - 2)

print(fibo(4)) # fibo(2) + fibo(1) + fibo(2) = 3
# => 시간복잡도 O(2**N)
# => 동일한 함수가 반복적으로 호출되는 문제점

# ✔ 메모이제이션(Memoization): 다이나믹 프로그래밍을 구현하는 방법 중 하나
# : 다이나믹 프로그래밍을 구현하는 방법 중 한 종류로, 한 번 구한 결과를 메모리 공간에 메모해두고 같은 식을 다시 호출하면 메모한 결과를 그대로 가져오는 기법
# => 값을 저장하는 방법이므로 캐싱이라고도 함.

# ◽ Code 2(다이나믹 프로그래밍): 탑다운 방식에 메모이제이션 기법 도입
# 한 번 계산된 결과를 메모이제이션(Memoization)하기 위한 리스트 초기화
d = [0] * 100

def fibo(x):
    if x == 1 or x == 2:
        return 1
    if d[x] != 0:
        return d[x]
    d[x] = fibo(x-1) + fibo(x-2)
    return d[x]
print(fibo(99))
# => 시간복잡도: O(N)
# 바로 아래 코드에서 호출되는 함수를 확인해보자
d = [0] * 100
def pibo(x):
    print('f(' + str(x) + ')', end=' ')
    if x == 1 or x == 2:
        return 1
    if d[x] != 0:
        return d[x]
    d[x] = pibo(x-1) + pibo(x-2)
    return d[x]
pibo(6) # f(6) f(5) f(4) f(3) f(2) f(1) f(2) f(3) f(4)

# WAY2: 반복문 (보텀업 방식: 작은 문제부터 차근차근 답을 도출)
# : 다이나믹 프로그래밍을 할 시, 재귀 함수 대신에 반복문을 사용하여 오버헤드를 줄일 수 있다.
# cf. 오버헤드(overhead)는 어떤 처리를 하기 위해 들어가는 간접적인 처리 시간 · 메모리 등을 말한다.
d = [0] * 100
d[1] =1
d[2] = 1
n = 99
for i in range(3, n+1):
    d[i] = d[i-1] + d[i-2]
print(d[n])

# 탑다운(메모이제이션) 방식은 '하향식'이라고도 하며, 보텀엄 방식은 '상향식'이라고도 한다.
# 다이나믹 프로그래밍의 전형적인 형태는 보텀업 방식이다.
# 보텀엄 방식에서 사용되는 결과 저장용 리스트는 'DP 테이블'이라고 부르며, '메모이제이션'은 탑다운 방식에 국한되어 사용되는 표현
# 엄밀히 말하면, 메모이제이션은 이전에 계산된 결과를 일시적으로 기록해 놓는 넓은 개념을 의미하므로, 다이나믹 프로그래밍과는 별도로 구분
# 한 번 계산된 결과를 어딘가에 담아 놓기만 하고 다이나믹 프로그래밍을 위해 활용하지 않을 수 있기 때문

# + 메모이제이션은 때에 따라서 리스트 자료형 말고도 사전(dict) 자료형을 이용할 수 있음. 
# => 예를 들어, an을 계산하고자 할 때, a0~a(n-1) 모두가 아닌 일부의 작은 문제에 대한 해답만 필요한 경우
# + 특정한 문제를 완전 탐색 알고리즘으로 접근할 때, 시간이 매우 오래 걸린다면, 다이나믹 프로그래밍으로!
# => 일단 단순히, 재귀함수로 비효율적인 프로그램을 작성한 뒤에, 메모이제이션을 적용할 수 있다면 이를 활용하여 코드를 개선
# => 또한 가능하다면 탑다운 방식보다는 보텀업 방식으로 구현. 시스템상 재귀함수의 스택 크기가 한정되어 있을 수 있기 때문
# => setrecursionlimit() 함수를 호출하여 재귀 제한을 완화할 수 있기는 함.

# ✅ 1로 만들기
x = int(input())
d = [0] * 30001
for i in range(2, x+1):
  d[i] = d[i-1] + 1
  if i % 2 == 0:
    d[i] = min(d[i], d[i//2]+1)
  if i % 3 == 0:
    d[i] = min(d[i], d[i//3]+1)
  if i % 5 == 0:
    d[i] = min(d[i], d[i//5]+1)
print(d[x])
# 숫자 1은 조건하에서 뺄 수도 나눌 수도 없으므로, 범위 안에 포함되지 않았다. 따라서 숫자 1에 대해선 어떠한 연산도 수행하지 않으므로 d[1] = 0 이다.

# ✅ 개미 전사
n = int(input())
array = list(map(int, input().split()))
d = [0] * 100
d[0] = array[0]
d[1] = max(array[0], array[1])
for i in range(2, n):
  d[i] = max(d[i-1], d[i-2] + array[i])
print(d[n-1])

# ✅ 바닥 공사
n = int(input())
d = [0] * 1001
d[1] = 1
d[2] = 3
for i in range(3, n+1):
  d[i] = (d[i-1] + 2 * d[i-2]) % 796796

print(d[n])

# ✅ 효율적인 화폐 구성
n, m = map(int, input().split())
coin = []
d = [10001] * (m+1)
d[0] = 0
for _ in range(n):
  coin.append(int(input()))

for i in coin:
  k = i # k = 2
  while k <= m:
    if k == i:
      d[k] = 1
    else:
      d[k] = min(d[k], d[k-i] + 1)
    k += i

d[m] = -1 if d[m] == 10001 else d[m]
print(d[m])

# ✅ 정수 삼각형
n = int(input())
data = [[0] * i for i in range(1,n+1)]
result = [[0] * i for i in range(1, n+1)]
for i in range(n):
  data[i] = list(map(int, input().split()))

result[0][0] = data[0][0]

# 행
for i in range(1,n):
# 열
  for j in range(0, i+1):
    if 0<=j<i:
      result[i][j] = max(result[i][j], result[i-1][j] + data[i][j])
    if 1<=j<(i+1):
      result[i][j] = max(result[i][j], result[i-1][j-1] + data[i][j])

print(max(result[n-1]))

# ✅ 못생긴 수
n = int(input())

ugly = [0] * n
ugly[0] = 1

i2 = i3 = i5 = 0
next2, next3, next5 = 2, 3, 5

for i in range(1,n):
  ugly[i] = min(next2, next3, next5)
  if ugly[i] == next2:
    i2 += 1
    next2 = ugly[i2] * 2
  if ugly[i] == next3:
    i3 += 1
    next3 = ugly[i3] * 3
  if ugly[i] == next5:
    i5 += 1
    next5 = ugly[i5] * 5

print(ugly[n-1])


# ✅ 퇴사
# ✔ 인덱스 활용 주의 ⭐⭐
# : -가 붙은 인덱스가 반복문 과정에서 부호가 바뀔 수 있음을 주의
# ✔ 경계점 주의: i + data[i][0] == n 일때가 경계임.
n = int(input())
data = []
result = [0] * n
for _ in range(n):
  t, p = map(int, input().split())
  data.append((t, p))
# n-1부터 0번째 인덱스까지 거꾸로 확인
for i in range(n-1, -1, -1):
  if i + data[i][0] == n:
    result[i] = data[i][1]
  elif i + data[i][0] < n:
    result[i] = data[i][1] + max(result[i+data[i][0]:])
print(max(result))

# ✅ 병사 배치하기
# => 전형적인 '가장 긴 증가하는 부분 수열 찾기' 문제
n = int(input())
data = list(map(int, input().split()))
data.reverse()
result = [1] * n
for i in range(1, n):
  for j in range(0, i):
    if data[i] > data[j]:
      result[i] = max(result[i], result[j]+1)
print(n-max(result))
