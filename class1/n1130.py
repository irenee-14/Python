'''
1130 - 두 수 비교하기
2022.8.30
'''

a, b = map(int, input().split())

if a > b:
    print(">")
elif a < b:
    print("<")
else:
    print("==")
