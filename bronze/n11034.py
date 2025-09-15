'''
2025.9.15
11034 - 캥거루 세마리 2
'''

while 1:
    try:
        A, B, C = map(int, input().split())
        print(max(B-A, C-B)-1)
    except:
        break