from numpy import *

def rotate(a, number, time, flag):
    for j in range(1,time+1):
        if not flag:
            a = a.T.copy()
        b = a.copy()
        for i in range(number):
            b[:,i] = a[:, number-1-i]
        a = b.copy()
    return b

def comparison(a,b):
    temp = a == b
    answer = True
    for i in range(N):
        for j in range(N):
            if not temp[i,j]:
                answer = temp[i,j]
    return answer

with open('transform.in', 'r') as f:
    N = int(f.readline().strip('\n'))
    square = [f.readline().strip('\n') for i in range(N*2)]

original = [square[i][j] for i in range(N) for j in range(N)]
transform = [square[i][j] for i in range(N, N*2) for j in range(N)]
original = array(original).reshape(N,N)
transform = array(transform).reshape(N,N)

with open('transform.out', 'w') as f:
    if comparison(transform, rotate(original, N, 1, 0)):
        f.write('1')
    elif comparison(transform, rotate(original, N, 2, 0)):
        f.write('2')
    elif comparison(transform, rotate(original, N, 3, 0)):
        f.write('3')
    elif comparison(transform, rotate(original, N, 1, 1)):
        f.write('4')
    elif (comparison(transform, rotate(rotate(original, N, 1, 1), N, 1, 0)))|(comparison(transform, rotate(rotate(original, N, 1, 1), N, 2, 0)))|(comparison(transform, rotate(rotate(original, N, 1, 1), N, 3, 0))):
        f.write('5')
    elif comparison(transform, original):
        f.write('6')
    else:
        f.write('7')
