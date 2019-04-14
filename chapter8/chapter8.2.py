fhand = open('mbox-short.txt')
count = 0
for line in fhand :
   # print(line)
    if line.startswith('From'):
        line=line.split()
        count =count + 1
        print(line[1])

print("total mails are:", count)


