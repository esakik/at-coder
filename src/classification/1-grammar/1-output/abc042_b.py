# https://atcoder.jp/contests/abc042/tasks/abc042_b

n, l = map(int, input().split())
s = sorted([input() for _ in range(n)])
print("".join(s))
