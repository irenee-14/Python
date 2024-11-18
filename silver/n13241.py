'''
2024.11.18
13241 - 최소공배수
'''


def _gcd(a, b):
    while a % b != 0:  # 나머지가 0이 되는 순간 멈춘다(최대공약수를 찾았다)
        tmp = a % b  # 갭을 줄이며 위치를 바꿔준다
        a = b
        b = tmp
    return b # 작은수를 리턴


def _lcm(a, b):
    return a * b // _gcd(a, b)


A, B = map(int, input().split())
print(_lcm(A, B))