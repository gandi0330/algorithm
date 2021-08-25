import sys
n = int(input())


pre_layer = [int(input())]

for layer in range(2,n+1):
    cur_layer = list(map(int,sys.stdin.readline().split()))
    for i in range(len(cur_layer)):
        if i == 0 :
            cur_layer[0] += pre_layer[0]
        elif i == len(cur_layer) - 1:
            cur_layer[-1] += pre_layer[-1]
        else:
            cur_layer[i] += max(pre_layer[i-1], pre_layer[i])
    
    pre_layer = cur_layer

print(max(pre_layer))