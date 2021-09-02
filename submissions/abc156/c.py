n = int(input())
x = list(map(int, input().split()))
l = 1000000000
for i in range(1, 101):
  l = min(l, sum([(x[j] - i)**2 for j in range(n)]))

print(l)
