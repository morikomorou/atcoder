n = int(input())
cnt = 0
magic = ''
for i in range(120):
  if n == 0:
    break
  if n % 2 == 0:
    n //= 2
    magic = 'B' + magic
    cnt += 1
  else:
    n -= 1
    magic = 'A' + magic
    cnt += 1
print(magic)
