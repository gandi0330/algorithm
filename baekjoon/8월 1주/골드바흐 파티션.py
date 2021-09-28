import sys

def era():
    era_list = [True] * (1000000 + 1)

    for i in range(2, int(1000000**0.5)):
        if era_list[i] == True:
            for j in range(i*2,1000000+1, i):
                era_list[j] = False
    
    era_list[0] = False
    era_list[1] = False
    
    return era_list


n = int(sys.stdin.readline())
num_list = [int(sys.stdin.readline()) for _ in range(n)]


era_list = era()

for num in num_list:
    case_count = 0
    for i in range(2, num//2+1):
        if era_list[i] and era_list[num-i] :
            case_count+=1
    
    print(case_count)