# url : https://www.acmicpc.net/problem/11723
# 난이도 : silver 5

import sys

n = int(input())

value = 0b100000000000000000000

for _ in range(n):
    command = sys.stdin.readline().rstrip().split()

    if command[0] == 'add' : 
        value = (value | 1 << int(command[1])-1)
    elif command[0] == 'check':
        if value & (1 << int(command[1])-1) > 0 :
            print(1)
        else:
            print(0)
    
    elif command[0] == 'remove':
        value = value & ~(1 << int(command[1])-1)
    
    elif command[0] == 'toggle':
       value = value ^ (1 << int(command[1])-1)

    elif command[0] == 'empty':
        value = 0b100000000000000000000
    
    elif command[0] == 'all':
        value = 0b111111111111111111111