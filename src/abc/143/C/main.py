# C - Slimes

N = int(input())  # Nひきのスライム, これらの色に関する情報が、長さNの英小文字から成る ex) 10
S = input()  # 文字列S ex) aabbbbaaca -> abaca


result = []
for i, s in enumerate(list(S)):
    if i == 0:
        result.append(s)
        continue

    if result[-1] == s:
        continue
    else:
        result.append(s)

print(len(result))
