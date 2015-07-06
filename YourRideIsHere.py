#set the dist
createVar = locals()
listTemp = range(1,27)
key = 65
for value in listTemp:
    createVar[chr(key)] = value
    key = key + 1

#get the value
def get_value(value):
    product = 1
    for item in value:
        product = product * ord(item)

    answer = product%47
    return answer

#get the input
while 1:
    print("please input the name of comet:")
    comet = raw_input()
    if len(comet) > 6:
        print("input length is too long!")
    elif not str.isalpha(comet):
        print("input format must be alpha!")
    elif not str.isupper(comet):
        print("input format must be upper!")
    else:
        break

while 1:
    print("please input the name of group:")
    group = raw_input()
    if len(group) > 6:
        print("input length is too long!")
    elif not str.isalpha(group):
        print("input format must be alpha!")
    elif not str.isupper(group):
        print("input format must be upper!")
    else:
        break

#get the answer
if get_value(comet) == get_value(group):
    print("GO")
else:
    print("STAY")
