a, b = map(int, input().split())
plug = 1
i = 0
while plug < b:
  plug += a - 1
  i += 1

print(i)
