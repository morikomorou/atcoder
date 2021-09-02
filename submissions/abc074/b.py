n = int(input())
k = int(input())
x = list(map(int, input().split()))
sum_x = 0
for i in range(n):
  sum_x += min(x[i], k-x[i])
print(sum_x * 2)
