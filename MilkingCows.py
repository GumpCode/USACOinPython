start = 0
end = 1
with open('milk2.in', 'r') as f:
    number1 = number2 = int(f.readline())
    time_table = [[0 for i in range(2)] for j in range(number1)]
    for line in f.readlines():
        time_table[number1-1] = line.strip('\n').split(' ')
        time_table[number1-1][start] = int(time_table[number1-1][start])
        time_table[number1-1][end] = int(time_table[number1-1][end])
        number1 = number1 - 1
time_table.sort()
milk = [0 for i in range(number2-1)]
nomilk = [0 for i in range(number2-1)]
for i in range(1,number2):
    if time_table[i][start] < time_table[i-1][end]:
        time_table[i][start] = time_table[i-1][start]
    if time_table[i][end] < time_table[i-1][end]:
        time_table[i][end] = time_table[i-1][end]
    milk[i-1] = time_table[i][end] - time_table[i][start]
for j in range(1,number2):
    if time_table[j][start] > time_table[j-1][end]:
        nomilk[j-1] = time_table[j][start] - time_table[j-1][end]
milk.sort(reverse = True)
nomilk.sort(reverse = True)
with open('milk2.out', 'w') as f:
    f.write(str(milk[0]))
    f.write(' ')
    f.write(str(nomilk[0]))
