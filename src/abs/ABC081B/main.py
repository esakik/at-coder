# Shift only


def check_if_even(a):
    if a % 2 == 0:
        return True
    else:
        return False


def check(inputs):
    alist = list(filter(check_if_even, inputs))
    if len(alist) == num:
        _inputs = [i // 2 for i in inputs]
        return _inputs


num = int(input())
inputs = [int(i) for i in input().split(' ')]

count = 0
while True:
    inputs = check(inputs)
    if inputs:
        count += 1
    else:
        break

print(count)
