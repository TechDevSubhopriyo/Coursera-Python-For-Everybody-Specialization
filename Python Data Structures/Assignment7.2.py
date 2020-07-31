fname = input("Enter file name: ")
fh = open(fname)
avg = 0.0
n = 0.0
c=0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    c=c+1
    pos = int(line.index(':'))
    n = n + float((line[pos+1:]).strip())
    
avg = n / c;
print('Average spam confidence:' , avg)
