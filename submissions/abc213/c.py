# ƒŠƒXƒg“à‚Ì—v‘f‚Ì‡ˆÊ‚ğæ“¾‚·‚é
def get_order(x):
  sorted_x = sorted(set(x))
  x_dict = {sorted_x[i]: i + 1 for i in range(len(sorted_x))}
  return [x_dict[i] for i in x]

h, w, n = map(int, input().split())
a, b = [0] * n, [0] * n
for i in range(n):
  a[i], b[i] = map(int, input().split())
a_order = get_order(a)
b_order = get_order(b)
for i in range(n):
  print('{} {}'.format(a_order[i], b_order[i]))
