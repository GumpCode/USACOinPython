#get the value
def get_value(value):
    product = 1
    for item in value:
        product = product * (ord(item)-64)
    answer = product%47
    return answer

i = 0
number = ['0', '0']
with open('ride.in','r') as f1:
    for line in f1.readlines():
        number[i] = line
        i = i+1

#get the answer
with open('ride.out', 'w') as f2:
    if get_value(number[0]) == get_value(number[1]):
        f2.write("GO")
    else:
        f2.write("STAY")
