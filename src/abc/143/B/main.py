# B - TAKOYAKI FESTIVAL 2019

N = int(input())
D = sorted(map(int, input().split()))

total = []
for i1, d1 in enumerate(D):
    for i2, d2 in enumerate(D):
        if i2 > i1:
            total.append(d1 * d2)

print(sum(total))
