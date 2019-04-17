import calendar
c = calendar.Calendar(0)
ll =[]
for i in range(1901, 2001):
    for j in range(1,13):
        ll+= c.monthdayscalendar(i, j)
sum = 0
for i in ll:
    if i[6] == 1:
        sum+=1
print(sum)