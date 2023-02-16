'''
2023.2.16
10808 - 알파벳 개수
'''
arr=input()
cnt=[0]*26

for i in arr:
    cnt[ord(i)-97]+=1

print(*cnt)
