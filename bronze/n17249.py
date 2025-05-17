'''
2025.5.17
17249 - 태보태보 총난타
'''

l, r = input().split("(^0^)")
cnt_l = 0
cnt_r = 0
for i in range(len(l)):
    if l[i] == '@':
        cnt_l += 1
for i in range(len(r)):
    if r[i] == '@':
        cnt_r += 1
print(cnt_l, cnt_r)