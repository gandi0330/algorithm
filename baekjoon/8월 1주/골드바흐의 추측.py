import sys

def era(max_num):
    era_list = [True] * (max_num + 1)

    for i in range(2, int(max_num**0.5)):
        if era_list[i] == True:
            for j in range(i*2, max_num+1, i):
                era_list[j] = False
    
    era_list[1] = False

    return era_list

num_list = []


while True:
    n = int(sys.stdin.readline())
    if n == 0 :
        break
    else : 
        num_list.append(n)

era_list = era(max(num_list))


for n in num_list :
    for i in range(3, n//2+1, 2):
        if era_list[i] and era_list[n-i] :
            print(f'{n} = {i} + {n-i}')

            break
    else :
        print('Goldbach\'s conjecture is wrong')