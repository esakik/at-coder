"""
A:
B:

- AとBの正の公約数の中からいくつか選ぶ
- ただし、選んだ整数の中のどの異なる2つの整数について、互いに素である必要がある。

公約数：x, y の両方で割切れること
互いに素：x, y の正の公約数が1のみであること

"""
from fractions import gcd as bltin_gcd


def coprime2(a, b):
    return bltin_gcd(a, b) == 1


def cf(x1,x2):
    cf = [1]
    for i in range(2, min(x1, x2) + 1):
        if x1 % i == 0 and x2 % i == 0:
            cf.append(i)
    return cf


A, B = map(int, input().split())

# 公約数
divisor_list = cf(A, B)

# print(divisor_list)

counts = []
for i in divisor_list:
    if i == 1:
        continue

    other_list = list(filter(lambda x: x != i, divisor_list))

    count = 0
    nums = []
    for j in other_list:
        if coprime2(i, j):
            for n in nums:
                if not coprime2(j, n):
                    break
            else:
                nums.append(j)
                count = count + 1

    counts.append(count)

if not counts:
    print(1)
else:
    print(max(counts) + 1)
