'''
2024.2.14
12904 - A와 B
'''

# 뒤에 A 추가 -> 뒤의 A 제거
# 뒤집고 뒤에 B 추가 -> B 제거하고 뒤집기 

# 맨 뒤부터 보기
# 뒤에 A가 있는 경우 / B가 있는 경우 

S = list(input())
T = list(input())

res = 0

while True:
    if S == T:
        res = 1
        break
    size = len(T)
    if size == 0:
        break 
    if T[size - 1] == 'A':
        del T[size - 1]
    elif T[size - 1] == 'B':
        del T[size - 1]
        T.reverse()
        
print(res)
