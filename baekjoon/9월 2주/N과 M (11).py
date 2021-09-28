from itertools import product

N, M = map(int,input().split())

num_list = sorted(map(int,input().split()))

for i in sorted(set(product(num_list, repeat=M))):
    print(' '.join(map(str,i)))