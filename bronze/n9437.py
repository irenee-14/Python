'''
2025.8.20
9437 - 사라진 페이지 찾기
'''

while 1:
    t = list(map(int, input().split()))
    if t[0] == 0:
        break
    for i in range(t[0]//4):
        tmp = [2*i+1, 2*i+2, t[0]-2*i-1, t[0]-2*i]
        if t[1] in tmp:
            tmp.remove(t[1])
            print(*tmp)