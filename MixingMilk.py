with open('milk.in', 'r') as f:
    input = f.readline().strip('\n').split(' ')
    total = int(input[0])
    farmer_num = int(input[1])
    number = [0 for i in range(farmer_num)]
    for i in range(farmer_num):
       number[i] = f.readline().strip('\n').split(' ')
    number.sort()

milk = 0
money = 0
for i in range(farmer_num):
    if (milk+int(number[i][1]))>=total:
        money += (total-milk)*int(number[i][0])
        break
    else:
        milk += int(number[i][1])
        money += int(number[i][0])*int(number[i][1])

with open('milk.out', 'w') as f:
    f.write(str(money))
