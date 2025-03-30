'''
2025.3.30
11098 - 첼시를 도와줘!
'''

n = int(input())

for _ in range(n):
    price = int(input())
    max_price = 0
    max_name = ""
    for _ in range(price):
        c, name = input().split()
        if int(c) > max_price:
            max_price = int(c)
            max_name = name

    print(max_name)
