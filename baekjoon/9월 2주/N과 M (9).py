from itertools import permutations

N, M = map(int,input().split())

num_list = sorted(map(int,input().split()))

for i in sorted(set(permutations(num_list, M))):
    print(' '.join(map(str,i)))
    