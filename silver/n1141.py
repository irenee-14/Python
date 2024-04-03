'''
2024.4.3
1141 - 접두사
'''
N = int(input())
word = []

for _ in range(N):
    word.append(input())
word.sort(key=len)

res = 0

for i in range(N):
    isPre = False 
    
    for j in range(i + 1, N):
        if word[i] == word[j][:len(word[i])]:
            isPre = True
            break 
    if not isPre:
        res += 1 

print(res)
