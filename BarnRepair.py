with open('barn1.in', 'r') as f:
    input = f.readline().strip('\n').split(' ')
    M_number = int(input[0])
    S_number = int(input[1])
    C_number = int(input[2])
    number = [0 for i in range(C_number)]
    i = 0
    for line in f.readlines():
        number[i] = int(line.strip('\n'))
        i = i+1

distance = [int(0) for i in range(C_number-1)]
number.sort()
for i in range(C_number-1):
    distance[i] = number[i+1] - number[i] - 1
distance.sort(reverse = True)
ChosenDistance = 0
for i in range(M_number-1):
    ChosenDistance = ChosenDistance + distance[i]
cost = number[C_number-1] - number[0] + 1 - ChosenDistance
with open('barn1.out', 'w') as f:
    f.write(str(cost))
