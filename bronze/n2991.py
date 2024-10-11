'''
2024.10.11
2991 - 사나운 개
'''

A, B, C, D = map(int, input().split())
delivery = map(int, input().split())


for i in delivery:
    dog = 0
    if 0 < i % (A + B) <= A:
        dog += 1
    if 0 < i % (C + D) <= C:
        dog += 1
    print(dog)
