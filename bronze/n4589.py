'''
2024.10.26
4589 - Gnome Sequencing
'''

n = int(input())

print("Gnomes:")
for i in range(n):
    tmp = list(map(int, input().split()))
    if tmp == sorted(tmp) or tmp == sorted(tmp, reverse=True):
        print("Ordered")
    else:
        print("Unordered")