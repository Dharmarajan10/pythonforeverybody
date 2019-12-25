hrs =input("Enter Hours:")
rph=input("enter rate per hour:")
h=float(hrs)
r=float(rph)
pay=40*r
xtrapay=pay+((h-40)*1.5*r)

def computepay(parameter1,parameter2): 
    if h<=40:
        return pay
    else:
        return xtrapay

x=computepay(h,r)
print(x)
