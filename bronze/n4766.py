'''
2025.5.16
4766 - 일반 화학 실험
'''

t1 = float(input())
while True:
    t2 = float(input())
    if t2 == 999:
        break
    print("%.2f" % (t2-t1))
    t1 = t2