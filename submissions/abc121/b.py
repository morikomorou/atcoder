n, m, c = map(int, input().split())
b = list(map(int, input().split()))
cnt = 0
for _ in range(n):
  a = list(map(int, input().split()))
  s = 0
  for j in range(m):
    s += a[j] * b[j]
  
  if s + c > 0:
    cnt += 1
print(cnt)
