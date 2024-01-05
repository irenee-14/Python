'''
2023.3.22
9625 - BABBA
'''

# b -> ba
# a -> b

# 1 -> 0 1
# 2 -> 1 1
# 3 -> 1 2
# 4 -> 2 3
# 5 -> 3 5 babbabab

n = int(input())

fi_a = [0, 0, 1]
fi_b = [0, 1, 1]

for i in range(3, n + 1):
    fi_a.append(fi_a[i - 2] + fi_a[i - 1])
    fi_b.append(fi_b[i - 2] + fi_b[i - 1])
print(fi_a[n], fi_b[n])

