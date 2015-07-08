with open('gift1.in', 'r') as f:
    number = int(f.readline().strip('\n'))
    name = [0 for i in range(number)]
    dict = {}
    for i in range(number):
        name[i] = f.readline().strip('\n')
        dict[name[i]] = 0
    for i in range(number):
        giver = f.readline().strip('\n')
        data = f.readline().strip('\n').split(' ')
        data = [int(data[i]) for i in range(2)]
        if not data[1]:
            dict[giver] = data[0]
        else:
            gift = int(data[0])/int(data[1])
            dict[giver] = dict[giver] - data[0] + (data[0] - gift*data[1])
        for j in range(data[1]):
            receiver = f.readline().strip('\n')
            dict[receiver] = dict[receiver] + gift

with open('gift1.out', 'w') as f:
    for i in range(number):
        f.write(name[i]+' '+str(dict[name[i]])+'\n')
