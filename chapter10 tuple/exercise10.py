fhand =open('mbox-short.txt')
d=dict()
for line in fhand:
    if line.startswith('From') and not line.startswith('From:'):
        hours= line.split(':')[0].split()[-1]
        if hours not in d:
            d[hours]=1
        else:
            d[hours]=d[hours]+1
for key,value in sorted(d.items()):
    print(key,value)


