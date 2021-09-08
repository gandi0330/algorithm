import sys

n,m = map(int,sys.stdin.readline().split())

matrix = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
answer = 0

def p1():
    global matrix, answer

    for _ in range(2):
        for i in range(len(matrix)-3):
            for j in range(len(matrix[0])):
                sub = matrix[i][j] + matrix[i+1][j] + matrix[i+2][j] + matrix[i+3][j]
                if answer < sub:
                    answer = sub
        rotate_90()
    


def p2():
    global matrix, answer

    for i in range(len(matrix)-1):
        for j in range(len(matrix[0])-1):
            sub = matrix[i][j] + matrix[i][j+1] + matrix[i+1][j] + matrix[i+1][j+1]
            if answer < sub:
                answer = sub

def p3():
    global matrix, answer

    for _ in range(2):
        for _ in range(4):
            for i in range(len(matrix)-2):
                for j in range(len(matrix[0])-1):
                    sub = matrix[i][j] + matrix[i+1][j] + matrix[i+2][j] + matrix[i][j+1]
                    if answer < sub:
                        answer = sub
        rotate_90()
    reverse_l_r()


def p4():
    global matrix, answer

    for _ in range(2):
        for _ in range(4):
            for i in range(len(matrix)-2):
                for j in range(len(matrix[0])-1):
                    sub = matrix[i][j] + matrix[i+1][j] + matrix[i+1][j+1] + matrix[i+2][j+1]
                    if answer < sub:
                        answer = sub
        rotate_90()
    reverse_l_r()

def p5():
    global matrix, answer

    for _ in range(4):
        for i in range(len(matrix)-1):
            for j in range(len(matrix[0])-2):
                sub = matrix[i][j] + matrix[i][j+1] + matrix[i+1][j+1] + matrix[i][j+2]
                if answer < sub:
                    answer = sub
        rotate_90()

def rotate_90():
    global matrix
    ref = [[0 for _ in range(len(matrix))] for _ in range(len(matrix[0]))]

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            ref[j][len(matrix)-i-1] = matrix[i][j]
    
    matrix = ref

def reverse_l_r():
    global matrix
    ref = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            ref[i][len(matrix[0])-j-1] = matrix[i][j]

    matrix = ref

p1()
p2()
p3()
p4()
p5()

print(answer)