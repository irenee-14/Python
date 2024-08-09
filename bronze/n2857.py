'''
2024.8.9
2857 - FBI
'''

res = []
for i in range(5):
    s = input()
    if 'FBI' in s:
        res.append(i + 1)

res.sort()
if res:
    print(*res, sep=' ')
else:
    print('HE GOT AWAY!')