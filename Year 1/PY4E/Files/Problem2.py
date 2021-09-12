file_name = input('Enter file name: ')
file = open(file_name)
cnt = 0
total = 0
for line in file:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    num = float(line[line.find('0') :])
    cnt += 1
    total += num
print('Average spam confidence:', total / cnt)
