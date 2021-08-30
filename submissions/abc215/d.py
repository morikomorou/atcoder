n, m = map(int, input().split())
a = map(int, input().split())

def get_prime(x):
  res = set()
  for i in range(2, int(x ** 0.5) + 1):
    while x % i == 0:
      x = x // i
      res.add(i)
  if x > 1:
  	res.add(int(x))
  return res

seen = set()
for i in a:
  seen |= get_prime(i)
res = [True] * m
ms = [i for i in range(1, m+1)]
for i in seen:
  for j in range(i, m + 1, i):
    res[j-1] = False
ans = []
for i in range(0,m):
  if res[i]:
    ans.append(i+1)
print(len(ans))
print(*ans, sep='\n')
