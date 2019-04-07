max_L=0
min_s=none
while 1:
    num = input('please enter number:')
    if num =='done':
        break
    else:
       try:
          num=int(num)
          if num>max_L:
             max_L=num
          elif num<min_s:
              min_s=num
       except:
          print('enter invalid number, please enter valid number')

print('large number is:',max_L )
print('samllest number is:',min_s)
