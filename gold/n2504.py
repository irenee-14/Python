'''
2024.5.17
2504 - 괄호의 값 (stack)
'''
s = list(input())

stack = []
res = 0 
tmp = 1

for i in range(len(s)):
    
    if s[i] == "(":
        stack.append(s[i])
        tmp *= 2
        
    elif s[i] == "[":
        stack.append(s[i])
        tmp *= 3
    
    elif s[i] == ")":
        if not stack or stack[-1] == "[":
            res = 0 
            break
        if s[i - 1] == "(":
            res += tmp 
        stack.pop()
        tmp //= 2 
    elif s[i] == "]":
        if not stack or stack[-1] == "(":
            res = 0 
            break
        if s[i - 1] == "[":
            res += tmp 
        stack.pop()
        tmp //= 3
        
if stack:
    print(0)
else:
    print(res)
