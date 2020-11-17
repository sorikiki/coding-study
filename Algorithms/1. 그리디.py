# 큰 수의 법칙
N, M, K = map(int, input().split())
li = list(map(int, input().split()))
li.sort()
x = li[N-1]
y = li[N-2] # it does not matter whether x and y are same with each other.
sum = 0
for i in range(1,M+1):
  if i % K == 0:
    sum += y
  else:
    sum += x
print(sum)

# 큰 수의 법칙(math가 가미된 것, 답안)
N, M, K = map(int, input().split())
li = list(map(int, input().split()))
li.sort()
x = li[N-1]
y = li[N-2] # it does not matter whether x and y are same with each other.
count = M // (K+1) * K
count += M % (K+1)

result = 0
result += count * x
result += (M-count) * y
print(result)

# 숫자 카드 게임
N, M = map(int, input().split())
li = []
for i in range(N):
  li2 = list(map(int, input().split()))
  li.append(min(li2))
print(max(li))

# 1이 될 때 까지(최대한 많이 나누기)
import time
N,K = map(int, input().split())
start_time = time.time()
result = 0
while N>=K:
  while N%K != 0:
    N -= 1
    result += 1
  N //= K
  result += 1
while N > 1:
  N -= 1
  result +=1
  print(result) 
end_time = time.time()
print(end_time-start_time)

# 모험가 길드
# 그룹 수가 최대가 되려면 그룹 당 구성원 수가 적어야 한다.
n = int(input())
li = list(map(int, input().split()))
# 오름차순으로 정렬
li.sort() 
group = 0
k = 0
for i in li:
  k += 1
  if k>=i:
    group += 1
    k = 0
print(group)

# 문자열 뒤집기 
s = input()
li = []
x = 2
for i in s:
  if x != i:
    li.append(i)
  x = i
zero = li.count('0')
one = li.count('1')
print(min(zero, one))

# 만들 수 없는 금액(집합 자료형의 활용)
import itertools
n = int(input())
li = list(map(int, input().split()))
answer = set()

for i in range(1, n+1):
  data = list(itertools.combinations(li, i))
  for j in data:
    answer.add(sum(j))
answer = set(range(1, max(answer)+1)) - answer
print(min(answer))

# 만들 수 없는 금액(해설, 그리디 알고리즘에 익숙해지기 ❗)
n = int(input())
data = list(map(int, input().split()))
data.sort()
target = 1
for x in data:
  if target < x:
    break
  target += x
print(target)

# 볼링공 고르기
n, m = map(int, input().split())
li = list(map(int, input().split()))
sum = 0
for i in range(0, len(li)):
  li2 = li[i+1:]
  sum += len(li2) - li2.count(li[i])
print(sum)