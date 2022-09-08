'''
2022.9.8
2908 - 상수
'''

n, m = input().split()
new_n = int(n[::-1])
new_m = int(m[::-1])
if new_n > new_m:
    print(new_n)
else:
    print(new_m)