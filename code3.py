
n=int(40)
hours = float(input("please input hours:"))
rate =input("please enter rate:")
rate=float(rate)
# if input hours > 40
if hours > n:
    pay = ((hours-n) * 1.5*rate) + (n * rate)
else:
    pay = hours * rate
print(pay)
