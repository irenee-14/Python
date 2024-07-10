'''
2024.7.10
2810 - 컵홀더
'''

N = int(input())
member = input()

count = member.count('LL')

if (count <= 1):
    print(len(member))
else:
    print(len(member) - count + 1)