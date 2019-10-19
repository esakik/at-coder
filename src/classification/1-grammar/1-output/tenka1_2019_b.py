# https://atcoder.jp/contests/tenka1-2019-beginner/tasks/tenka1_2019_b

n = int(input())
S = input()
k = int(input())

for s in S:
    print(s if s == S[k - 1] else "*", end="")
