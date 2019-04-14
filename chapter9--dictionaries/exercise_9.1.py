fhand= open('mbox-short.txt')
dd = dict()
for line in fhand:
    if line.startswith('From'):
       mail=line.split()[1]
       if mail not in  dd:
            dd[mail]=1
       else:
            dd[mail]=dd[mail]+1
max1 = 0
mail1= None
for key in dd:
    if dd[key]>max1:
        max1=dd[key]
        mail1=key

print("1.the send max mail name:",mail)
print("2.total send:",max1)

