name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
sender =dict()
l=list()
for line in handle:
    l=line.split();
    if('From ' in line):
        sender[l[1]] = sender.get(l[1],0) +1;

bigdata = None
bigvalue = None
for k,v in sender.items():
    if bigdata is None or v>bigvalue:
        bigdata = k
        bigvalue = v
print(bigdata,bigvalue)