n = int(input())
d = list(map(int, input().split()))
sorted_d = sorted(d)
k_max = sorted_d[n // 2]
k_min = sorted_d[n // 2 - 1]
if k_max != k_min:
  print(k_max - k_min)
else:
  print(0)
