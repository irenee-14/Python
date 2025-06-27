'''
2025.6.27
3058 - 짝수를 찾아라
'''

for _ in range(int(input())):
    li = list(map(int, input().split()))
    tmp = []
    for n in li:
        if n % 2 == 0:
            tmp.append(n)
    print(sum(tmp), min(tmp))