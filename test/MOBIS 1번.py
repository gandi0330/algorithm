from itertools import product, permutations

def solution(dice):
    
    com_list = []
    
    for i in range(len(dice)):
        sub_list = []
        for j in permutations(dice,i+1):
            sub_list += list(product(*j))
        com_list.append([''.join(map(str,tuple_)).lstrip('0') for tuple_ in sub_list])
    print(com_list) 
    for i in range(1, 10**len(dice)):
        d = len(str(i)) - 1
        
        if str(i) not in com_list[d]:
            return i

solution([[1, 6, 2, 5, 3, 4], [9, 9, 1, 0, 7, 8]])