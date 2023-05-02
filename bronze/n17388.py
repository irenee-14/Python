'''
2023.5.2
17388 - 와글와글 숭고한
'''

s, k, h = map(int, input().split())
if s + k + h >= 100:
    print("OK")
else:
    res = min(s, k, h)
    if res == s:
        print("Soongsil")
    elif res == k:
        print("Korea")
    else:
        print("Hanyang")
