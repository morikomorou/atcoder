from itertools import permutations
s, k = input().split()
k = int(k)
res = set()
for i in permutations(s):
  text = ''.join(i)
  res.add(text)
  text = ''
res_list = list(res)
std = sorted(res_list)
print(std[k - 1])
