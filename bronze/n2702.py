'''
2024.11.26
2702 - 초6 수학
'''

def _gcd(a, b):
    while a % b != 0:  # 나머지가 0이 되는 순간 멈춘다(최대공약수를 찾았다)
        tmp = a % b  # 갭을 줄이며 위치를 바꿔준다
        a = b
        b = tmp
    return b # 작은수를 리턴


def _lcm(a, b):
    return a * b // _gcd(a, b)


n = int(input())

for i in range(n):
    a, b = map(int, input().split())
    print( _lcm(a, b), _gcd(a, b))