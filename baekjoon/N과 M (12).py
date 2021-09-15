from itertools import combinations_with_replacement

N, M = map(int,input().split())

num_list = sorted(map(int,input().split()))

for i in sorted(set(combinations_with_replacement(num_list,M))):
    print(' '.join(map(str,i)))