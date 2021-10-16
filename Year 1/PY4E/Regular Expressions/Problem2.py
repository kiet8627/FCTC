import re
import statistics 
file = open(input('Enter file: '))
numList = list()
for line in file:
    line = line.rstrip()
    s = re.findall('^New Revision: ([0-9]+)', line)
    if len(s) != 1: continue
    num = int(s[0])
    numList.append(num)
print(int(statistics .mean(numList)))
        
