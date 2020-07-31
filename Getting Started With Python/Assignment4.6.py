def computepay(h,r):
    p =  0.0
    if(h <= 40):
        p=h*r
    else:
        p=(40*r)+((h-40)*r*1.5)
    return p

hrs = float(input("Enter Hours:"))
rate = float(input("Enter rate: "))
p = computepay(hrs,rate)
print("Pay",p)