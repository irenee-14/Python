'''
2024.7.1
24183 - Affischutskicket
'''

c4, a3, a4 = map(int, input().split())
C4 = c4 * 0.229 * 0.324
A3 = a3 * 0.297 * 0.42
A4 = a4 * 0.21 * 0.297
print("%.3f" % (2 * C4 + 2 * A3 + A4))
