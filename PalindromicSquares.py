dict = {0:'0', 1:'1', 2:'2', 3:'3', 4:'4', 5:'5', 6:'6', 7:'7', 8:'8', 9:'9', 10:'A', 11:'B', 12:'C', 13:'D', 14:'E', 15:'F', 16:'G', 17:'H', 18:'I', 19:'J'}
def BitTransform(value, bit):
    number = []
    while value>0:
        number.append(dict[value%bit])
        value = value/bit
    number.reverse()
    temp = ''
    for num in number:
        temp += num
    return temp

def PalindromicJudge(number):
    flag = True
    for i in range(len(number)/2):
        if number[i] != number[len(number)-i-1]:
            flag = False
    return flag

with open('palsquare.in', 'r') as f:
    bit = int(f.readline().strip('\n'))

with open('palsquare.out', 'w') as f:
    for i in range(1,301):
        number = BitTransform(i*i, bit)
        if PalindromicJudge(number):
            f.write(BitTransform(i, bit)+' '+ number +'\n')
