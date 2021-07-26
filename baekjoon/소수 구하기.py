n,m = map(int,input().split())

era = [True] * m

k = int(m ** 0.5)

for i in range(2, k + 1):
    if era[i] == True:
        for j in range(i * 2, m, i):
            era[j] = False

era[1] = False

for i in range(n,m+1):
    if era[i] == True:
        print(i)

# 예를 들어 17의 소수를 구한다
# 보통 약수는 대칭 구조이고 그 중간은 수의 제곱근이기 때문에
# 중간까지만 약수가 있는지 확인하면 된다