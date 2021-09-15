# url : https://www.acmicpc.net/problem/1107
# 난이도 : gold 5

# 입력 채널
channel = int(input())

# 고장난 번호 개수
k = int(input())


# a는 입력 채널에서 하나씩 올라가는 채널, b는 내려가는 채널
a, b = channel, channel

# answer는 입력 채널에서 현재 채널까지의 거리로 초기화
answer = abs(channel - 100)

# 고장난 번호가 1개 이상일 때 
if k > 0:
    # 고장난 번호 입력받기
    breakdown = list(map(int,input().split()))

    # 채널을 선택할 때 고장나지 않은 번호들로만 구성되있으면 True
    c = False

    # 입력받은 채널로부터 위로 아래로 한칸씩 가며 고장나지 않은 번호들로 구성되어 있을 때
    # 번호 길이와 , 정답 채널과의 거리 차이를 더해 answer와 비교하여 작은 값을 출력
    while True:
        
        # a
        if b >= 0 :
            b_list = list(map(int,str(b)))

            for i in set(b_list):
                if i in breakdown:
                    b -= 1
                    break
            else:
                c = True

            if answer < len(str(b)) + channel - b :
                print(answer)
                break

            if c == True:
                print(len(str(b)) + channel - b)
                break
            
                
        
        a_list = list(map(int,str(a)))
        
        if breakdown:
            for i in set(a_list):
                if i in breakdown:
                    a += 1
                    break
            else:
                c = True
        
        if answer < len(str(a)) + a - channel :
                print(answer)
                break

        if c == True:
            print(len(str(a)) + a- channel)
            break
else:
    print(min(answer, len(str(channel))))
    



    


