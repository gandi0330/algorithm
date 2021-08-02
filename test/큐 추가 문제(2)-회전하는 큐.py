n, _ = map(int,input().split())
pick_list = list(map(int, input().split()))

que_ = [i+1 for i in range(n)]

min_distance_count = 0

now_idx = 0

for num in pick_list :
    new_idx = que_.index(num)
    distance = max(new_idx,now_idx) - min(new_idx, now_idx)

    if distance > len(que_)/2 :
        distance = len(que_) - distance
    
    min_distance_count += distance
    que_.remove(que_[new_idx])
    now_idx = new_idx

print(min_distance_count)