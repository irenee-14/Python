'''
2025.10.31
17869 - Simple Collatz Sequence
'''

count = 0
n = int(input())
while n != 1:
    n = n + 1 if n % 2 == 1 else n // 2
    count += 1
print(count)