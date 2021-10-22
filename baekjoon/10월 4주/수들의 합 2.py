# url : https://www.acmicpc.net/problem/2003
# 난이도 : silver 3

n,m = map(int,input().split())

num_list = [*map(int,input().split())]


start = 0 
end = 0

cnt = 0
while end <n:

    if sum(num_list[start:end+1]) == m :
        cnt += 1
        start+=1
        end = start+1
    
    elif sum(num_list[start:end+1]) > m :
        start += 1
    
    elif sum(num_list[start:end+1]) < m :
        end += 1

print(cnt)