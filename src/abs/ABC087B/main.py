# Coins

A = int(input())  # 500円玉 枚数
B = int(input())  # 100円玉 枚数
C = int(input())  # 50円玉 枚数
X = int(input())  # 合計金額

count = 0
for i in range(A + 1):
    for j in range(B + 1):
        for k in range(C + 1):
            sum = i * 500 + j * 100 + k * 50

            if X == sum:
                count += 1

print(count)
