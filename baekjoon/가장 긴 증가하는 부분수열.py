_ = input()

num_list = list(map(int,input().split()))




start_idx = 0
while True:
    min_num = num_list[start_idx]
    length = 1

    sub_list = []
    length_list = []
    for i in range(1,len(num_list[start_idx+1:])):

        if num_list[i] > min_num:
            length += 1
            min_num = num_list[i]
        
        if num_list[start_idx] > num_list[i]:
            sub_list.append(i)

        
    length_list.append(length)

    if sub_list :
        start_idx = sub_list[0]
    else :
        break

print(max(length_list))