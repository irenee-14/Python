'''
2024.12.9
1817 - 짐 챙기는 숌
'''

n, m = map(int, input().split())
if n == 0:
    print(0)
else:
    books = list(map(int, input().split()))
    weight = 0
    count = 1
    for book in books:
        if book + weight <= m:
            weight += book
        else:
            weight = book
            count += 1
    print(count)