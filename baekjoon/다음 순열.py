# # url = https://www.acmicpc.net/problem/10972
# # silver 3


# n = int(input())

# num_list = list(map(int,input().split()))

# answer = []

# if num_list == list(range(n,0,-1)) :
#     print(-1)
# else:

#     for i in range(1, len(num_list)):
#         if num_list[i:] == sorted(num_list[i:])[::-1] :
#             if len(num_list[:i]) >= 2 :
#                 left_list = num_list[:i]
#             else:
#                 left_list = []

#             sub_list = sorted(num_list[i:])
#             sub_list.remove(num_list[i-1]+1)

#             right_list = [num_list[i-1]+1] + sub_list

# print(left_list+right_list)


n = int(input())
num_list = list(map(int,input().split()))

from itertools import permutations

pm = [[*i] for i in permutations([i for i in range(1,n+1)],n)]
for idx, i in enumerate(pm):
    if i == num_list:
        if len(i)-1 == idx : 
            print(-1)
        else:
            print(' '.join(map(str,pm[idx+1])))
    print(idx, i)