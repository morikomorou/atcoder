import math
n = int(input())
x = [n // 1.08, n // 1.08 + 1]
flg = 0
for i in x:
  if math.floor(int(i) * 1.08) == n:
    print(int(i))
    flg = 1
    break

if flg == 0:
  print(':(')
