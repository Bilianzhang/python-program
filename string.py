str = 'X-DSPAM-Confidence:0.8475'
pos=str.find('5')
print(pos)
val=float(str[pos])
print(val)
