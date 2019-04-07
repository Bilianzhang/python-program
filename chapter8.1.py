fhand= open('filetest.txt')
wordslist=[]
for line in fhand:
    # print(line)
    words = line.split()
    # print(words)
    for word in words:
        if word in wordslist:
            continue
        else:
            wordslist.append(word);
#
wordslist.sort()
print(wordslist)
