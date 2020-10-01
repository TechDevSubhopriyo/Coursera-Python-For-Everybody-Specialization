import re

sum = 0
x = open('regex_sum_802363.txt').read()
lst = re.findall('[0-9]+',x)
for num in lst:
    sum = sum + int(num)
print(sum)
