ONES = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight",
        "nine", "ten"]
TEENS = ["zero", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen",
        "seventeen", "eighteen", "nineteen"]
TENS = ["zero","ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy",
        "eighty", "ninety"]

def numtowords(num):
    num = str(num)
    if len(num) > 3: return
    h, t, o = (None, None, None)
    if len(num) == 3:
        h, t, o = num
    elif len(num) == 2:
        t, o = num

    if int(t) == 1:
        return "{h} hundred {t}".format(h=ONES[int(h)],
                                        t=TEENS[int(o)])
    elif int(t) == 0:
        return "{h} hundred {o}".format(h=ONES[int(h)],
                                        o=ONES[int(o)])
    else:
        return "{h} hundred {t} {o}".format(h=ONES[int(h)],
                                            t=TENS[int(t)],
                                            o=ONES[int(o)])

print 315, numtowords(315)
print 855, numtowords(855)
print 602, numtowords(602)
