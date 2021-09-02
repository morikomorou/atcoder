a, b, c = map(int, input().split())
cnt = 0
flg = 0
if a == b == c != 1:
  print(-1)
else:
  while (a % 2 == 0) and (b % 2 == 0) and (c % 2 == 0):
    if a == b == c:
      print(-1)
      flg = 1
      break
    aa = (b + c) // 2
    bb = (a + c) // 2
    cc = (a + b) // 2
    a = aa
    b = bb
    c = cc
    cnt += 1
  if flg != 1:
    print(cnt)
