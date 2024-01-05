'''
2023.1.5
1629 - 곱셈
'''

import sys
input = sys.stdin.readline

a, b, c = map(int, input().split())

def multiple(a, n):
  if (n == 1):
      return a % c
  else:
      tmp = multiple(a, n // 2)
      if n % 2 == 0:
          return (tmp * tmp) % c
      else:
        return (tmp  * tmp * a) % c

print(multiple(a,b))
