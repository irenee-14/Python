'''
2025.5.15
10419 - 지각
'''

for _ in range(int(input())):
    n = int(input())
    t = 0
    while (t+1) + (t+1)**2 <= n:
        t += 1
    print(t)