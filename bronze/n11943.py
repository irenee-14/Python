'''
2023.3.31
11943 - 파일 옮기기
'''

a, b = map(int, input().split())
c, d = map(int, input().split())

print(min(a + d, b + c))