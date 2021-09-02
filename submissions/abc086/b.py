a, b = input().split()
x = int(a + b)
flg = 0
for i in range(500):
  if i ** 2 == x:
    flg = 1
if flg:
  print('Yes')
else:
  print('No')
