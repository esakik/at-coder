# Kagami Mochi

# N枚の円形の餅
N = int(input())

all = list(set([int(input()) for _ in range(N)]))

alist = []
while True:
    if not alist:
        index = all.index(max(all))
        alist.append(all.pop(index))

    if not all:
        break

    if max(all) < min(alist):
        index = all.index(max(all))
        alist.append(all.pop(index))
    else:
        break

print(len(alist))
