# D - Triangles

N = int(input())  # N本の棒
L = sorted(map(int, input().split()))  # i本目の棒の長さはLi
length = len(L)


count = 0
for x in range(length):
    a = L[x]

    for y in range(x + 1, length):
        b = L[y]

        for z in range(y + 1, length):
            c = L[z]

            if (a < b + c) and (b < c + a) and (c < a + b):
                count += 1

print(count)
