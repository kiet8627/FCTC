file = open(input('Enter a file name: '))
d = dict()
l = list()
for c in range(ord('a'), ord('z') + 1):
    d[chr(c)] = 0
for line in file:
    line = line.lower()
    for word in line:
        if 'a' <= word and word <= 'z':
            d[word] += 1
for key, val in list(d.items()):
    l.append((val, key))
for val, key in sorted(l, reverse = True):
    print(key, val)
