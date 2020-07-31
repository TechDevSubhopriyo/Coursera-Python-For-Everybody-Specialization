name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

time = dict()
for line in handle:
    if line.startswith('From '):
        words = line.split()
        time[words[5][0:2]]=time.get(words[5][0:2],0) + 1
        
lst = list()
for k,v in time.items():
    lst.append((k,v))

lst = sorted(lst)
for k,v in lst:
    print(k,v)