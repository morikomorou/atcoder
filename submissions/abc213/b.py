n = int(input())
a = list(map(int, input().split()))
a_dict = {a[i]: i for i in range(n)}
sorted_a = sorted(a)
print(a_dict[sorted_a[-2]] + 1)
