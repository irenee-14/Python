'''
2024.3.1 
10799 - 쇠막대기
'''
laser = input()

stack = []
cnt = 0

for i in range(len(laser)):
    if laser[i] == '(':
        stack.append('(')
        
    else:
        stack.pop()
        if laser[i - 1] == '(':
            cnt += len(stack)
        else:
            cnt += 1 
print(cnt)
    
