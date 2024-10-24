'''
2024.10.24
1340 - 연도 진행바
'''

month_name_li = ["January" , "February", "March", "April", "May", "June",
            "July", "August", "September", "October", "November", "December"]
month_day_li = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

month, D, Y, T = input().split()
D = int(D[:-1])
Y = int(Y)
H, M = map(int, T.split(':'))

if Y % 400 == 0 or (Y % 4 == 0 and Y % 100 != 0):
    month_day_li[1] += 1
total = sum(month_day_li) * 24 * 60

last_month = month_name_li.index(month)
current = (sum(month_day_li[:last_month]) + D - 1) * 24 * 60 + H * 60 + M
print(current/total * 100)
