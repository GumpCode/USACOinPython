keyword = ['', '', 'ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PRS', 'TUV', 'WXY']

with open('dict.txt', 'r') as f:
    dict = [0 for i in range(5000)]
    dict = f.readline().strip('\n').split(' ')
    answer = [1 for i in range(len(dict))]
with open('namenum.in', 'r') as f:
    number = f.readline().strip('\n')

for order in range(len(number)):
    num = int(number[order])
    for name in dict:
        if (keyword[num][0]!=name[order])&(keyword[num][1]!=name[order])&(keyword[num][2]!=name[order]):
            index = dict.index(name)
            answer[index] = 0

with open('namenum.out', 'w') as f:
    flag = 0
    for i in range(len(answer)):
        if answer[i] == 1:
            f.write(dict[i]+'\n')
            flag = 1
    if flag ==0:
        f.write('NONE')
