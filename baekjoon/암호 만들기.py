from itertools import combinations

l,c = map(int,input().split())

alpha_list = input().split()

vowel = ['a','e','i','o','u']

answer = []
for tuple_ in combinations(alpha_list, l):
    for char in tuple_:
        if char in vowel :
            strs= ''.join(sorted(tuple_))
            if strs not in answer:
                answer.append(strs)
            
            break

for list_ in sorted(answer):
    print(list_)