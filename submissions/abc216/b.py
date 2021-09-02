n = int(input())
s = [''] * n
t = [''] * n
flg = 0
for i in range(n):
  s[i], t[i] = input().split()
for i in range(n):
  if flg:
    break
  for j in range(i+1, n):
    if s[i] == s[j]:
      if t[i] == t[j]:
        print('Yes')
        flg = 1
        break
if flg == 0:
	print('No')
