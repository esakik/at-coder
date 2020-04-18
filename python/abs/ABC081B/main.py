# Shift only

N = int(input())
A = list(map(int, input().split()))

count = 0
while True:
    if N == len([i for i in A if i % 2 == 0]):
        A = [i // 2 for i in A]
        count += 1
    else:
        break

print(count)
