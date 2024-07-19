'''
2024.7.19
27182 - Rain Diary
'''
n, m = map(int, input().split())

if n > 7:
    print(n - 7)
else:
    print(m + 7)