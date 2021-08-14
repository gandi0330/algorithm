n = int(input())

num_list = [*map(int, input().split())]


# sum_left = 0
# answer_list = []
# for num in num_list:
#     if num >= 0 :
#         sum_left += num
#     elif num < 0 and sum_left+num > 0 :
#         answer_list.append(sum_left)
#         sum_left += num
#     else:
#         answer_list.append(sum_left)
#         sum_left = 0

# answer_list.append(sum_left)

# if max(answer_list) == 0:
#     print(max(num_list))
# else:
#     print(max(answer_list))

sum_sub = answer = -1000

for num in num_list:
    sum_sub = max(num, sum_sub + num)
    answer  = max(sum_sub,answer)

print(answer)