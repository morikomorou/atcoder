n, a, b = map(int, input().split())
s = input()
pass_num = 0
pass_num_b = 0
for i in range(n):
  if s[i] == 'c' or pass_num >= a + b:
    print('No')
  elif s[i] == 'a' and pass_num < a + b:
    print('Yes')
    pass_num += 1
  elif s[i] == 'b':
    pass_num_b += 1
    if pass_num < a + b and pass_num_b <= b:
      print('Yes')
      pass_num += 1
    else:
      print('No')
  else:
    print('No')
