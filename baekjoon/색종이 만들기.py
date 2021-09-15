import sys

def dc (num_list):
    global white, blue
    
    if len(num_list) == 1:
        if num_list[0] ==[0] :
            white+=1
            return None
        else:
            blue += 1
            return None

    for i in range(len(num_list)):
        if set(num_list[i]) == {0} : pass
        else : 
            break
    else : 
        white+= 1
        return None
    for i in range(len(num_list)):
        if set(num_list[i]) == {1} : pass
        else : 
            break
    else : 
        blue+= 1
        return None

    l = len(num_list)//2

    num_list1 = []
    num_list2 = []
    num_list3 = []
    num_list4 = []

    for i in range(0,l):
        num_list1.append(num_list[i][:l])
        num_list2.append(num_list[i][l:])
    
    for i in range(l,len(num_list)):
        num_list3.append(num_list[i][:l])
        num_list4.append(num_list[i][l:])

    return dc(num_list1), dc(num_list2), dc(num_list3), dc(num_list4)


n = int(input())
num_list = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]

white = 0
blue = 0

dc(num_list)

print(white, blue)

