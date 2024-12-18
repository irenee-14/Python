'''
2024.12.18
22988 - 재활용 캠페인(투포인터)
'''

N, X = map(int, input().split())
arr = sorted(list(map(int, input().split())))

s = 0
e = N - 1

cnt = 0
remain = 0

while s <= e: # s와 e가 교차되면 멈춘다!
    if arr[e] == X:
        cnt += 1
        e -= 1
        continue
    if s == e: # 만나면 짜투리 추가
        remain += 1
        break

    if arr[e] + arr[s] >= X / 2:
        cnt += 1
        s += 1
        e -= 1
    else:
        s += 1 # 수가 커짐
        remain += 1
print(cnt + remain // 3) ## 빈 병 3개가 있을 때 1병을 만들 수 있음
# 0 + 0 -> 6.5
# 6.5 + 0 -> 6.5
