'''
2022.10.13
1978 - 소수찾기
'''
import math
import sys
input = sys.stdin.readline

def check_prime(n):
    if n==0 or n==1:
        return False
    else:
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True


n = int(input())
n_num = list(map(int, input().split()))
count = 0

for i in n_num:
    if check_prime(i):
        count += 1
print(count)