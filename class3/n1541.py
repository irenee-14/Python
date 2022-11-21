'''
2022.11.21
1541 - 잃어버린 괄호
'''

st = input().split('-')
res = 0

for i in range(len(st)):
    cnt = 0
    s = st[i].split('+')
    for j in s:
        cnt += int(j)
    if i == 0:
        res = cnt
        #print(i, res)
    else:
        res -= cnt
        #print(i, res)
print(res)
