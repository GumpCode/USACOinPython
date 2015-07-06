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
    comet = raw_input("please enter the name of comet:")
    if len(comet) > 6:
        print("input length is too long!")
    elif not str.isalpha(comet):
        print("input format must be alpha!")
    elif not str.isupper(comet):
        print("input format must be upper!")
    else:
        break

while 1:
    group = raw_input("please enter the name of group:")
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
