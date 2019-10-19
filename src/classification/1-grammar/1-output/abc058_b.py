# https://atcoder.jp/contests/abc058/tasks/abc058_b

O = list(input())
E = list(input())

for o, e in zip(O, E):
    print(o + e, end="")
