'''
2023.12.21
6568 - 귀도 반 로썸은 크리스마스날 심심하다고 파이썬을 만들었다 (2진수)
'''

import sys
input = sys.stdin.readline

while True:
    adder = 0
    pc = 0
    mem = [0 for _ in range(32)]
    for i in range(32):
        try:
            mem[i] = int(input(), 2)
        except:
            exit()
    
    while True:
        operator = mem[pc] >> 5
        operand = mem[pc] % 32
        pc = (pc + 1) % 32
        
        if operator == 0:
            mem[operand] = adder
        elif operator == 1:
            adder = mem[operand]
        elif operator == 2:
            if adder == 0:
                pc = operand
        elif operator == 3:
            continue
        elif operator == 4:
            adder = (adder - 1) % 256
        elif operator == 5:
            adder = (adder + 1) % 256
        elif operator == 6:
            pc = operand
        elif operator == 7:
            break
    
    print(format(adder, '08b'))
