'''
2025.2.27
3986 - 좋은 단어
'''

n = int(input())
res = 0

for i in range(n):
    stack = []
    line = list(input())

    for x in line:
        if not len(stack):
            stack.append(x)
        elif stack[-1] == x:
            stack.pop(-1)
        else:
            stack.append(x)
    if not len(stack):
        res += 1

print(res)