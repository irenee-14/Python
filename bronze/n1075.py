'''
2023.4.2
1075 - 나누기
'''

n = input()
f = int(input())
cut = int(n[:-2] + '00')

while True:
    if cut % f == 0:
        break
    cut += 1
print(str(cut)[-2:])