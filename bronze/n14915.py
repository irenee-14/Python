'''
2025.11.5
14915 - 진수 변환기
'''

def convert(n, base):
    T = "0123456789ABCDEF"
    q, r = divmod(n, base)
    return convert(q, base) + T[r] if q else T[r]


a, b = map(int, input().split())
print(convert(a, b))