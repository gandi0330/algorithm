# 링크 https://www.acmicpc.net/problem/1931

import sys

n = int(input())
num_list = []

for _ in range(n):
    start, end = map(int,sys.stdin.readline().split())
    num_list.append([start,end])

num_list = sorted(num_list, key=lambda x : (x[1],x[0]))

now_meeting =  num_list[0]
cnt = 1

idx = 1

while idx < len(num_list):
    if now_meeting[1] <= num_list[idx][0]:
        now_meeting = num_list[idx]
        cnt+=1
    
    idx +=  1

print(cnt)