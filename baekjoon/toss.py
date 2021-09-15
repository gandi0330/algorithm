seconds = 300

seconds = int(str(seconds)[:-1])
dp_table = [91] * (seconds + 1)
dp_table[0] = 0
snacks = {30 : 10, 13 : 30, 12 : 20, 2 : 30}

for sec in range(1,seconds+1):
    select_snack = [[dp_table[sec], 0]]

    if sec - 30 >= 0 and snacks[30] >= 0:
        select_snack.append([dp_table[sec - 30] + 1, 30])
    if sec - 13 >= 0 and snacks[13] >= 0:
        select_snack.append([dp_table[sec - 13] + 1, 13])
    if sec - 12 >= 0 and snacks[12] >= 0:
        select_snack.append([dp_table[sec - 12] + 1, 12])
    if sec - 2 >= 0 and snacks[2] >= 0:
        select_snack.append([dp_table[sec - 2] + 1, 2])
    
    min_ = 91
    
    for snack in select_snack:
        if snack[0] < min_:
            min_ = snack[0]
            decrease_snack = snack[1]
    
    dp_table[sec] = min_

    if decrease_snack != 0:
        snacks[decrease_snack] -= 1
