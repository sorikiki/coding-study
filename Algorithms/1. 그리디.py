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