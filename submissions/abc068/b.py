n = int(input())
max_num = 1
max_cnt = 0
for i in range(1, n+1):
  cnt = 0
  y = i
  while y % 2 == 0:
    y //= 2
    cnt += 1
  if cnt > max_cnt:
    max_cnt = cnt
    max_num = i
print(max_num)
