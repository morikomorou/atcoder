n, m = map(int, input().split())
k = [0] * m
a = []
ontop = {i: [] for i in range(1, n + 1)}
que = []
flg = 0
for i in range(m):
  k[i] = int(input())
  a.append(list(map(int, input().split()))[::-1])
  top_color = a[i][-1]
  ontop[top_color].append(i)
  if len(ontop[top_color]) == 2:
    que.append(ontop[top_color])

for i in range(n):
  if len(que):
    for j in que[0]:
      a[j].pop()
      if len(a[j]) > 0:
        top_color = a[j][-1]
        ontop[top_color].append(j)
        if len(ontop[top_color]) == 2:
          que.append(ontop[top_color])
    que.pop(0)
  else:
    flg = 1
    print('No')
    break
if flg != 1:
  print('Yes')
