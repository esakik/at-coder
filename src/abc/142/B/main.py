"""
N: N人
K: Kcm 以上必要
"""
N, K = map(int, input().split())

count = 0
h = map(int, input().split())

for i in h:
    if i >= K:
        count = count + 1

print(count)
