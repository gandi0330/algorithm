strs_minus = input().split('-')

for i in range(len(strs_minus)):
    strs_plus = strs_minus[i].split('+')
    strs_minus[i] = sum([int(j.lstrip('0')) for j in strs_plus ])

if len(strs_minus) == 1:
    print(strs_minus[0])
else:
    print(strs_minus[0] - sum([i for i in strs_minus[1:]]))
    
