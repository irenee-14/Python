'''
2024.4.6
1434 - 책 정리
'''


N, M = map(int, input().split())
boxes = list(map(int, input().split()))
books = list(map(int, input().split()))

print(sum(boxes) - sum(books))