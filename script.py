def computepay(h,r):
    if 0 < h <= 40 and r > 0:
        regHrs = h
        totalPay = regHrs * r
    elif h > 40 and r > 0:
        otHrs = h - 40
        regHrs = h - otHrs
        regPay = regHrs * r
        otPay = otHrs * r * 1.5
        totalPay = regPay + otPay
    else:
        return 0
    return totalPay

hrs = input("Enter Hours: ")
try:
    h = float(hrs)
except:
    print("Enter a correct hour value")
    quit()
pay = input("Enter Rate: ")
try:
    r = float(pay)
except:
    print("Enter a correct pay rate")
    quit()
p = computepay(h,r)
print("Pay",p)
