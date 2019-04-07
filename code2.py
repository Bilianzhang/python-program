rate1 = float(1.0)
rate2 = float(3.0)
n=int(40)
hours = float(input("please input hours:"))

# if input hours > 40
if hours > n:
    pay = ((hours-n) * rate2) + (n * rate1)
else:
    pay = hours * rate1
print(pay)
