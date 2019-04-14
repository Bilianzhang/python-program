max_L=True
min_s=None
while 1:
    num = input('please enter number:')
    if num =='done':
        break
    else:
       try:
            num=int(num)

            if max_L is True:
                 max_L=num
            elif num>max_L:
                 max_L=num

            if min_s is None:
                 min_s=num
            elif num < min_s:
                 min_s=num
       except:
          print('enter invalid number, please enter valid number')

print('large number is:',max_L )
print('samllest number is:',min_s)
