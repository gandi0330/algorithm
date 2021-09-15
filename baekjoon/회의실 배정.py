# 링크 https://www.acmicpc.net/problem/1931

import sys

n = int(input())
num_list = []

# 2차원 리스트로 입력받기
for _ in range(n):
    start, end = map(int,sys.stdin.readline().split())
    num_list.append([start,end])

# 끝나는 시간으로 오름차순 정렬 후 끝나는 시간이 같으면 시작 시간을 오름차순 정렬
num_list = sorted(num_list, key=lambda x : (x[1],x[0]))

# 첫 미팅
now_meeting =  num_list[0]
cnt = 1
idx = 1

# 이전 회의의 끝나는 시간보다 크거나 같은 시작 시간을 찾으면 현재 회의를 바꾸고 카운팅
while idx < len(num_list):
    if now_meeting[1] <= num_list[idx][0]:
        now_meeting = num_list[idx]
        cnt+=1
    
    idx +=  1

print(cnt)