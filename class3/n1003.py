'''
2022.11.11
1003 - 피보나치 함수
'''
def fib(n):
    zero = [1, 0, 1]
    one = [0, 1, 1]
    length = len(zero)
    if n >= length:
        for i in range(length, n+1):
            zero.append(zero[i-1] + zero[i-2])
            one.append(one[i-1] + one[i-2])
    print(zero[n], one[n])

T = int(input())
for i in range(T):
    fib(int(input()))
