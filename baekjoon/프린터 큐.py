import sys
from collections import deque

n = int(input())

for _ in range(n):
    n, m  = map(int, sys.stdin.readline().split())
    num_dq = deque([*map(int,sys.stdin.readline().split())])

    cnt = 0
    while True:
        if num_dq[0] == max(num_dq):
            num = num_dq.popleft()

            if num == num_dq[m] :
                break
            else:
                cnt += 1
                m = m - 1
                num_dq.append(num)

        
        else :
            num = num_dq.popleft()
            if num == num_dq[m] :
                break
            else:
                cnt += 1
                num_dq.append(num)