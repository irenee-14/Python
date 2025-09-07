'''
2025.9.7
7510 - 고급 수학
'''

for i in range(int(input())):
    li = sorted(map(int, input().split()))
    if li[0]**2 + li[1]**2 == li[2]**2:
        print(f"Scenario #{i+1}:")
        print("yes\n")
    else:
        print(f"Scenario #{i+1}:")
        print("no\n")