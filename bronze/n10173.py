'''
2025.6.9
10173 - 니모를 찾아서
'''

while True:
    s = input()
    if s == "EOI":
        break
    print("Found" if "nemo" in s.lower() else "Missing")
