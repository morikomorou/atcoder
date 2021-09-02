k, n = map(int, input().split())
a = list(map(int, input().split()))
min_len = 1000000000
for i in range(n):
  if i == 0:
    min_len = min(min_len, a[-1] - a[0])
  else:
    min_len = min(min_len, a[i - 1] + k - a[i])
print(min_len)
