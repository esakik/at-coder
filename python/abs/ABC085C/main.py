# Otoshidama

# お札がN枚, 合計でY円
N, Y = map(int, input().split())

if Y % 10000 == 0:
    alist = reversed(range(N + 1))
else:
    alist = range(N + 1)

for x in alist:
    if (10000 * x == Y) and (x == N):
        print('{} {} {}'.format(x, 0, 0))
        break

    for y in range(N + 1):
        if (10000 * x + 5000 * y == Y) and (x + y == N):
            print('{} {} {}'.format(x, y, 0))
            break

        for z in range(N + 1):
            if (10000 * x + 5000 * y + 1000 * z == Y) and (x + y + z == N):
                print('{} {} {}'.format(x, y, z))
                break
        else:
            continue
        break
    else:
        continue
    break
else:
    print('-1 -1 -1')
