'''
2024.2.1
5800 - 성적 통계
'''

import sys
input = sys.stdin.readline

k = int(input())
for i in range(k):
    grades = list(map(int, input().split()))
    sortGrade = sorted(grades[1::], reverse=True)
   
    gap = sortGrade[0] - sortGrade[1]
    for j in range(2, len(sortGrade)):
        gap = max(gap, sortGrade[j - 1] - sortGrade[j])
    
    print("Class", i+1)
    print("Max ", max(sortGrade), ", Min ", min(sortGrade), ", Largest gap ", gap, sep='')
