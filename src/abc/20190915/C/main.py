# Attack Survival

"""
ラウンドの参加者：N人（1からNまでの番号）
ラウンド開始時点では全員がKポイント
誰かが問題に正解すると、その人以外のN−1人のポイントが1減ります
ラウンド終了時にポイントが 0以下の参加者は敗退し、残りの参加者が勝ち抜けます
このラウンドでは Q回の正解が出て、i番目に正解したのは参加者Aiでした。
キザハシ君の代わりに、N人の参加者のそれぞれが勝ち抜けたか敗退したかを求めるプログラムを作成してください。

N K Q
A1
A2
.
.
.
AQ
"""

n, k, q = map(int, input().split())
answer = [int(input()) for _ in range(q)]

for i, _ in enumerate(range(n), 1):
    if k - (q - answer.count(i)) > 0:
        print('Yes')
    else:
        print('No')
