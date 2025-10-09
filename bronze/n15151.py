'''
2025.10.9
15151 - Incomplete Book
'''

# k, d = map(int, input().split())
# days = [0] * d
# days[0] = k
# res = 1
#
# for i in range(1, d):
#     days[i] = days[i - 1] * 2
#     if sum(days) <= d:
#         res = i + 1
# print(res)

k, d = map(int, input().split())

total_days = 0
books = 0
days_per_book = k

while total_days + days_per_book <= d:
    total_days += days_per_book
    books += 1
    days_per_book *= 2

print(books)