# from itertools import permutations

# n = int(input())

# num_list = list(map(int,input().split()))

# oper = ['+','-','*','/']

# oper_list = []

# for idx, num in enumerate(map(int,input().split())):
#     for _ in range(num):
#         oper_list.append(oper[idx])

# min_value = 1000000000
# max_value = -1000000000

# for opers in set(permutations(oper_list,n-1)):
#     sub = num_list[0]
#     opers = [*opers]
#     for i in range(n-1):
#         if opers[i] == '+':
#             sub += num_list[i+1]
#         elif opers[i] =='-':
#             sub -= num_list[i+1]
#         elif opers[i] == '/':
#             if sub > 0:
#                 sub //= num_list[i+1]
#             else:
#                 sub = -(-sub // num_list[i+1])
#         else:
#             sub *= num_list[i+1]
    
#     if sub >  max_value:
#         max_value = sub

#     if sub < min_value:
#         min_value = sub


# print(max_value)
# print(min_value)


n = int(input())

num_list = list(map(int,input().split()))

a,b,c,d = map(int,input().split())

max_value = -1000000000
min_value = 1000000000

def permutation(result,  num_idx, a,b,c,d):
    global max_value, min_value

    
    if num_idx == n :
        max_value = max(max_value, result)
        min_value = min(min_value, result)
        return
    
    if a : 
        permutation(result + num_list[num_idx], num_idx + 1, a-1, b, c, d)
    if b : 
        permutation(result - num_list[num_idx], num_idx + 1, a, b-1, c, d)
    if c : 
        permutation(result * num_list[num_idx], num_idx + 1, a, b, c-1, d)
    if d : 
        permutation(int(result / num_list[num_idx]), num_idx + 1, a, b, c, d-1)

permutation(num_list[0],1,a, b, c, d)

print(max_value)
print(min_value)