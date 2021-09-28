from itertools import combinations

l,c = map(int,input().split())

alpha_list = input().split()

vowel = ['a','e','i','o','u']

answer = []
for tuple_ in combinations(alpha_list, l):
    vowel_cnt = 0
    conso_cnt = 0
    for char in tuple_:
        if char in vowel :
            vowel_cnt += 1
        else :
            conso_cnt += 1
    
    if vowel_cnt >= 1 and conso_cnt>= 2:

        strs= ''.join(sorted(tuple_))
        if strs not in answer:
             answer.append(strs)
            
            

for list_ in sorted(answer):
    print(list_)