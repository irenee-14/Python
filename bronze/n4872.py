'''
2024.8.29
4872 - SPIN
'''


start = input().strip()
D = len(start)

spin = [int(x) for x in start]

while True:
    try:
        s = input().strip()
        if s == "":
            break
        for i in range(D):
            spin[i] += int(s[i])
    except EOFError:
        break
for i in range(D):
    print(spin[i] % 10, end='')