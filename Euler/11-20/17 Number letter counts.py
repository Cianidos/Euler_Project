ddd = {
    '0': '',
    '1': "one",
    '2': "two",
    '3': "three",
    '4': "four",
    '5': "five",
    '6': "six",
    '7': "seven",
    '8': "eight",
    '9': "nine",
    '10': "ten",
    '11': "eleven",
    '12': "twelve",
    '13': "thirteen",
    '14': "fourteen",
    '15': "fifteen",
    '16': "sixteen",
    '17': "seventeen",
    '18': "eighteen",
    '19': "nineteen",
    '20': "twenty",
    '30': "thirty",
    '40': "forty",
    '50': "fifty",
    '60': "sixty",
    '70': "seventy",
    '80': "eighty",
    '90': "ninety",
    '100': "hundred",
    '1000': "thousand"
}

x = 1000
su = ""
for x in range(10, 20):
    for ind, s in enumerate(str(x)[::-1]):
        if ind == 0:
            su += ddd.get(s)
            #print("%5d  %3s  %3s  %3s" % (int(s) * 10 ** ind, su, ddd.get(s), s))
        if ind == 1:
            su += ddd.get(str(int(s) * 10 ** ind))
            #print("%5d  %3s  %3s  %3s" % (int(s) * 10 ** ind, su, ddd.get(str(int(s) * 10 ** ind)), s))
        if ind == 2 and s!='0':
            su += (ddd.get(s) + "and" + ddd.get(str(10 ** 2)))
            #print("%5d  %3s  %3s  %3s" % (int(s) * 10 ** ind, su, ( ddd.get(s) + "and" + ddd.get(str(10 ** ind) )), s))
        if ind == 3:
            su += ddd.get(s) + ddd.get(str(10**ind))
            #print("%5d  %3s  %3s  %3s" % (int(s) * 10 ** ind, su, ( ddd.get(s) + "and" + ddd.get(str(10 ** ind) )), s))
    print("----------------------------")
print("%s \n %d" % (su, su.__len__()))
