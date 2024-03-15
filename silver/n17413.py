'''
2024.3.9
17413 - 단어 뒤집기2
'''
S = input()
stack = []
res = ''
inner = False

for x in S:
    if x == '<':
        inner = True 
        for _ in range(len(stack)):
            res+= stack.pop()
    stack.append(x)
    
    if x == '>':
        inner = False 
        for _ in range(len(stack)):
            res += stack.pop(0)
    
    if x == ' ' and not inner:
        stack.pop()
        for i in range(len(stack)):
            res += stack.pop()
        res += ' '
if stack:
    for i in range(len(stack)):
        res+= stack.pop()
print(res)
    
