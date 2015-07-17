with open('friday.in', 'r') as f:
    n = int(f.readline())
week = [0 for i in range(1,8)]
month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31 ]
date = 3
for year in range(1900, 1900+n):
    if ((year%4==0)&(year%100!=0))|((year%100==0)&(year%400==0)):
        month[1] = 29
        for number in range(0,12):
            date = ((date+month[number-1])%7)
            week[date-1] = week[date-1] + 1
    else:
        month[1] = 28
        for number in range(0,12):
            date = ((date+month[number-1])%7)
            week[date-1] = week[date-1] + 1
with open('friday.out', 'w') as f:
    for i in range(-2,5):
        f.write(str(week[i])+' ')
