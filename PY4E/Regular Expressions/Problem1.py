import re
file = open('mbox.txt')
inp = input('Enter a regular expression: ')
cnt = 0
for line in file:
    if re.search(inp, line):
        cnt += 1
print('mbox.txt had', cnt, 'lines that matched', inp)
