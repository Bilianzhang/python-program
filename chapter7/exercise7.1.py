fname=input("please enter file name ")
fhand = open(fname)
count = 0
s = 0
v = 0
for line in fhand :
   # print(line)
    if line.startswith('X-DSPAM-Confidence:'):
        line=line.split()

        s = s + float(line[1])
        count = count + 1

v = s/count
print("average is:", v)
print("total is :", count)