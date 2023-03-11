'''
2023.3.11
5397 - 키로거
'''

n = int(input())

for _ in range(n):
    pw = input()
    left = []
    right= []
    for x in pw:
        if x =='<':
            if left:
                right.append(left.pop())
        elif x == '>':
            if right:
                left.append(right.pop())
        elif x == '-':
            if left:
                left.pop()
        else:
            left.append(x)
            
    left.extend(reversed(right))
    print(''.join(left))
            
