'''
2025.1.30
7572 - 간지(干支)
'''


twelve = 'ABCDEFGHIJKL'
ten = '0123456789'

n = int(input()) - 2013

print(twelve[(n + 5) % 12] + ten[(n - 1) % 10])