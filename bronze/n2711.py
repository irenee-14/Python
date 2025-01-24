'''
2025.1.24
2711 - 오타맨 고창영
'''

for _ in range(int(input())):
    n, string = input().split()
    n = int(n)
    print(string[:n-1], string[n:], sep='')