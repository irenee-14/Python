'''
2024.2.28
1431 - 시리얼 번호
'''
def sum_serial(serial):
    res = 0
    for i in serial:
        if i.isdigit():
            res += int(i)
    return res

n = int(input())

serial = []
for i in range(n):
    serial.append(input())
    
serial.sort(key = lambda x:(len(x), sum_serial(x), x))
print(*serial, sep="\n")
