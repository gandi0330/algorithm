from itertools import combinations

N, M = map(int,input().split())

num_list = sorted(map(int,input().split()))

for i in sorted(set(combinations(num_list, M))):
    print(' '.join(map(str,i)))
    