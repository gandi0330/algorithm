from collections import deque

n = int(input())

deq = deque(map(int,input().split()))

answer = []
idx = 0
while deq:
    answer.append(idx+1)

    idx += deq.pop(idx) - 1

    if idx >=0 : idx = idx % len(deq)
    else : 
