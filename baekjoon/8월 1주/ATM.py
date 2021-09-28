# 링크 https://www.acmicpc.net/problem/11399

_ = input()

num_list = sorted(map(int,input().split()))

wait_time = 0
answer_li = []
for num in num_list:
    wait_time += num
    answer_li.append(wait_time)

print(sum(answer_li))