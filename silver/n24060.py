'''
2025.3.13
24060 - 알고리즘 수업 - 병합 정렬 1
'''


def merge_sort(s, e):
    if s < e:
        m = (s + e) // 2
        merge_sort(s, m)
        merge_sort(m + 1, e)
        merge(s, m, e)


def merge(s, m, e):
    i = s
    j = m + 1
    t = s

    while i <= m and j <= e:
        if A[i] <= A[j]:
            result.append(A[i])
            tmp[t] = A[i]
            t += 1
            i += 1
        else:
            result.append(A[j])
            tmp[t] = A[j]
            t += 1
            j += 1

    while i <= m:
        result.append(A[i])
        tmp[t] = A[i]
        t += 1
        i += 1
    while j <= e:
        result.append(A[j])
        tmp[t] = A[j]
        t += 1
        j += 1

    i = s
    t = s
    while i <= e:
        A[i] = tmp[t]
        i += 1
        t += 1


a, k = map(int, input().split())
A = list(map(int, input().split()))
tmp = list(0 for _ in range(a))
result = []
merge_sort(0, a - 1)

if k <= len(result):
    print(result[k - 1])
else:
    print(-1)

