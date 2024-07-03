'''
2024.7.4
17009 - Winning Score
'''

line1 = [int(input()) for _ in range(3)]
line2 = [int(input()) for _ in range(3)]
A = line1[0] * 3 + line1[1] * 2 + line1[2]
B = line2[0] * 3 + line2[1] * 2 + line2[2]

if A == B:
    print("T")
elif A > B:
    print("A")
else:
    print("B")