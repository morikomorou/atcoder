x, y = map(int, input().split())
flg = 0
for i in range(0, x + 1):
  if flg:
    break
  for j in range(0, x + 1):
    if i + j > x:
      break
    elif 10000 * i + 5000 * j + 1000 * (x - i - j) == y:
      text = '{} {} {}'.format(i, j, x - i - j)
      flg = 1
      break

if flg:
  print(text)
else:
  print('-1 -1 -1')
