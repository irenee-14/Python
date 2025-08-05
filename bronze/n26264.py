'''
2025.8.5
26264 - 빅데이터? 정보보호!
'''

N = int(input())
attention = input()
bigData = attention.count('bigdata')
seCurity = attention.count('security')

if bigData > seCurity:
    print('bigdata?')
elif bigData < seCurity:
    print('security!')
else:
    print('bigdata? security!')