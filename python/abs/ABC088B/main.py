# Card Game for Two

# N枚のカード
N = int(input())
# i枚目のカードにはaiの数字が書かれている
a = list(map(int, input().split()))

alice = []
bob = []
for i in range(N):
    index = a.index(max(a))

    if i % 2 == 0:
        alice.append(a.pop(index))
    else:
        bob.append(a.pop(index))

print(sum(alice) - sum(bob))
