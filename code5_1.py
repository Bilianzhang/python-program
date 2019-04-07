h=input("please enter you hours:")
r=input("please enter you rate:")

try:
    h1=int(h)
    print("enter hours:" , h1)
except:
    print("invalid hour,please input digits")

try:
    r1=int(r)
    print("enter rate:" , r1)
except:
    print("invalid rate,please input digits")
