'''
2025.8.9
23805 - 골뱅이 찍기 - 돌아간 ㄹ
'''

n = int(input())
for i in range(n):
    for j in range(n):
        print("@@@",end="")
    for j in range(n):
        print(" ",end="")
    for j in range(n):
        print("@",end="")
    print()

for i in range(n):
    for k in range(3):
        for j in range(n):
            print("@",end="")
        for j in range(n):
            print(" ",end="")
        for j in range(n):
            print("@",end="")
        for j in range(n):
            print(" ",end="")
        for j in range(n):
            print("@",end="")
        print()

for i in range(n):
    for j in range(n):
        print("@",end="")
    for j in range(n):
        print(" ",end="")
    for j in range(n):
        print("@@@",end="")
    print()