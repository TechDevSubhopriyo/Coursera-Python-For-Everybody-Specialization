hrs = input("Enter Hours:")
h = float(hrs)
rate = float(input("Enter Rate:"))
pay = 0
if h <= 40 : pay = rate * h
else : pay = (40 * rate) + ((h-40) * rate *1.5)
print(pay)