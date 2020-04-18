# Some Sums

# 1以上, N以下の整数、各桁の和がA以上B以下の総和
N, A, B = map(int, input().split())

total = 0
for i in range(1, N + 1):
    s = 0
    for j in str(i):
        s += int(j)

    if A <= s <= B:
        total += i

print(total)
