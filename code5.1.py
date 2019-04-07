def computepay(x,y):
    x=float(x)
    y=float(y)
    if x > 40:
        pay=(x-40) * 1.5*y + 40*y
    else:
        pay=x*y
    return pay
pay1= computepay('45','10.5')
print(pay1)
