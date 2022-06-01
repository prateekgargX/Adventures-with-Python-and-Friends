import re

handle = open('reg.txt','r')
sum=0
for line in handle:
    for num_s in re.findall('[0-9]+',line):
        sum+=float(num_s)
print(sum)
handle.close()