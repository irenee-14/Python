'''
2024.2.21
17091 - 숫자시계
'''
h = int(input())
m = int(input())

h_arr = ['one', 'two', 'three', 'four', 'five',
         'six', 'seven', 'eight', 'nine', 'ten',
          'eleven', 'twelve']
          
m_arr = ['one', 'two', 'three',
          'four', 'five', 'six', 'seven', 
          'eight', 'nine', 'ten', 'eleven', 
          'twelve', 'thirteen', 'fourteen', 
          'quarter', 'sixteen', 'seventeen',
          'eighteen', 'nineteen', 'twenty',
          'twenty one', 'twenty two', 'twenty three',
          'twenty four', 'twenty five', 'twenty six',
          'twenty seven', 'twenty eight', 'twenty nine',
          'half']

def clock(h, m, word):
    if m == 1:
        print(m_arr[m - 1], 'minute', word, h_arr[h - 1], sep=' ')
    elif m == 30 or m == 15:
        print(m_arr[m - 1], word, h_arr[h - 1], sep=' ')
    else:
        print(m_arr[m - 1], 'minutes', word, h_arr[h - 1], sep=' ')


if m == 0:
    print(h_arr[h - 1], 'o\' clock', sep=' ')
elif 1 <= m and m <= 30:
    clock(h, m, 'past')
else:
    m = 60 - m
    clock((h + 1) % 12, m, 'to')
