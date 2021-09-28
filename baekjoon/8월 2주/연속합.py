n = int(input())

num_list = [*map(int, input().split())]


sum_sub = answer = -1000

for num in num_list:
    sum_sub = max(num, sum_sub + num)
    answer  = max(sum_sub,answer)

print(answer)