'''
2022.9.28
11948 - 과목선택
'''
first = []
second = []
sub = 0
for _ in range(4):
    first.append(int(input()))
first.sort()
for i in range(1,4):
    sub += first[i]
for _ in range(2):
    second.append(int(input()))
second.sort()
sub += second[1]
print(sub)