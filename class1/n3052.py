'''
2022.9.9
3052 - 나머자
'''

remain = []

for num in range(10):
    remain.append(int(input()) % 42)
remain = set(remain)
print(len(remain))
