'''
2023.4.30
1076 - 저항
'''

color = ['black', 'brown', 'red', 'orange', 'yellow',
        'green', 'blue', 'violet', 'grey', 'white']
fir = color.index(input())
sec = color.index(input())
thr = color.index(input())
res = int(str(fir) + str(sec)) * (10 ** thr)
print(res)