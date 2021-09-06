import sys

def transpose(matrix):
    l = len(matrix)

    tp_matrix = []

    for i in range(l):
        sub_list = []
        for j in range(l):
            sub_list.append(matrix[j][i])
        tp_matrix.append(sub_list)
    
    return tp_matrix


def change():
    global  candy, candy2, n, max_answer
    
    for i in range(n):
        for j in range(n-1):
            

            candy[i][j], candy[i][j+1] = candy[i][j+1], candy[i][j]
            max_answer = check(candy, max_answer)
            print(candy)
            candy[i][j], candy[i][j+1] = candy[i][j+1], candy[i][j]
            

            candy2[i][j], candy2[i][j+1] = candy2[i][j+1], candy2[i][j]
            max_answer = check(candy2, max_answer)
            print(candy2)
            candy2[i][j], candy2[i][j+1] = candy2[i][j+1], candy2[i][j]
            

            if max_answer == n :
                return max_answer

    return max_answer

def check(matrix, max_answer):
    
    global candys, n


    for i in range(n):
        for c in candys:
            max_answer = max(max_answer, matrix[i].count(c))
    
    matrix = transpose(matrix)

    for i in range(n):
        for c in candys:
            max_answer = max(max_answer, matrix[i].count(c))

    return max_answer



n = int(input())

candy = [[*sys.stdin.readline().strip()] for _ in range(n)]
candys = ['C','P','Z','Y']
max_answer = 0

candy2 = transpose(candy)

print(change())


 