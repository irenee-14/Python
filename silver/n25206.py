'''
2024.10.17
25206 - 너의 평점은
'''

grade = {"A+" : 4.5, "A0" : 4.0,
         "B+" : 3.5, "B0" : 3.0,
         "C+": 2.5, "C0": 2.0,
         "D+": 1.5, "D0": 1.0,
         "F": 0.0}
res = 0
total = 0
for i in range(20):
    name, a, b = input().split()
    if b == "P":
        continue
    res += float(a) * grade[b]
    total += float(a)
print(f"{res / total:.6f}")