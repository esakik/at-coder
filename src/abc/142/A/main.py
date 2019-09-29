num = int(input())

count = 0
for i in range(num):
    if i % 2 == 0:
        count = count + 1

print(count / num)
