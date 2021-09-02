n = int(input())
a = list(map(int, input().split()))
dict_a = {a[i]: i + 1 for i in range(n)}
sorted_a = sorted(a)
res = [dict_a[sorted_a[i]] for i in range(n)]
print(*res)
