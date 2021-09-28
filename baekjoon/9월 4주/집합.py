import sys

n = int(input())

S = set()

for _ in range(n):
    command = sys.stdin.readline().rstrip().split()

    if command[0] == 'add' : 
        if command[1] not in S:
            S = S | set(command[1])

    elif command[0] == 'check':
        if command[1] in S :
            print(1)
        else:
            print(0)
    
    elif command[0] == 'remove':
        if command[1] in S:
            S = S - set(command[1])
    
    elif command[0] == 'toggle':
        if command[1] in S:
            S = S - set(command[1])
        else:
            S = S | set(command[1])

    elif command[0] == 'empty':
        S = {}
    
    elif command[0] == 'all':
        S = {i for i in range(1,21)}

    