'''
2022.9.21
2231 - 분해합
'''

n = int(input())
result = 0

for i in range(1, n+1):
    m_list = list(map(int, str(i)))
    result = i + sum(m_list)
    if result == n:
        print(i)
        break
    if i == n:
        print(0)
