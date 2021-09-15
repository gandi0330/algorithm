from itertools import combinations

n, s = map(int, input().split())

num_list = list(map(int,input().split()))
comb_list = []

for i in range(1,n+1):
    comb_list += list(combinations(num_list, i))

cnt = 0
for num_tuple in comb_list:
    if sum(num_tuple) == s:
        cnt += 1

print(cnt)