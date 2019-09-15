# Tap Dance

odd = ['R', 'U', 'D']
even = ['L', 'U', 'D']

inputs = input()

result = None
for i, s in enumerate(inputs):
    if (i + 1) % 2 == 0 and s in even:
        result = 'Yes'
    elif (i + 1) % 2 != 0 and s in odd:
        result = 'Yes'
    else:
        result = 'No'
        break

print(result)
