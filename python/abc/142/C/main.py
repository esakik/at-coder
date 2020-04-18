"""
N: N人クラス
A1 A2 … AN: 出席番号


"""

N = int(input())
A = list(map(int, input().split()))

nums = []
nos = []
for no in range(N):
    num = A[no]  # 1, num = 3
    nums.append(num)
    nos.append(no)

Z = [str(x + 1) for _, x in sorted(zip(nums, nos))]

print(' '.join(Z))
