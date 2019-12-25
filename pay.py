hrs = input("Enter Hours:")
h = float(hrs)
rph=input("Enter rate per hour:")
r=float(rph)
if h<=40:
    pay=r*h
    print("pay:",pay)
else:
    basicpay=40*r
    extrahr=(h-40)
    extrapay=extrahr*r*1.5
    print(basicpay+extrapay)
