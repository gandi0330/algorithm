def solution(a):
    
    answer = []
    for s in a:
        answer.append(cal(s))
    
    return answer
        
def cal (s):
    

    l = len(s)
    
    a_cnt = s.count('a')
    while True:
        
        if s == 'a' : 
            return True

        elif l > 1 and s[0] == 'a' :
            s = s[1:]
            l -= 1
            a_cnt-=1
        elif l > 1 and s[-1] == 'a' :
            s = s[:-1]
            l -= 1
            a_cnt-=1
        elif l >= 2*a_cnt and s[0:a_cnt] == 'b'*a_cnt and s[-1*a_cnt:] == 'b'*a_cnt :
            s = s[a_cnt:-a_cnt]
            l -= 2*a_cnt
        else:
            return False
