n = int(input())

num_list = list(map(int,input().split()))

partial_sum=[False]*(n*100000+1)

visited = {}

for num in num_list:
    if num not in visited:
        visited[num] = 1
    else:
        visited[num] += 1

def cal(now_depth,  visited, sub_sum):
    
    if now_depth == n :
        partial_sum[sub_sum] = True 
        return 

    for num in set(num_list):
        if visited[num] > 0:
            sub_sum += num
            partial_sum[sub_sum] = True
            visited[num] -= 1
            cal(now_depth+1,  visited, sub_sum)
            visited[num] += 1
            sub_sum -= num

cal(0,visited, 0)

i = 1
while True:
    if partial_sum[i] == True:
        i += 1
    else:
        print(i)
        break


# n = int(input())

# num_list = list(map(int,input().split()))

# partial_sum=[False]*(n*100000+1)


# def cal(i, sub_sum):
#     if i == n:
#         partial_sum[sub_sum] = True
#         return
#     cal(i+1,sub_sum+num_list[i])
#     cal(i+1,sub_sum)
    

# cal(0,0)

# i = 1
# while True:
#     if partial_sum[i] == True:
#         i += 1
#     else:
#         print(i)
#         break