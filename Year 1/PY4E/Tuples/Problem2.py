file = open(input('Enter a file name: '))
d = dict()
for line in file:
    if line.startswith('From') and not(line.startswith('From:')):
        word = line.split()
        try:
            d[word[5][: 2]] += 1
        except:
            d[word[5][: 2]] = 1

d = dict(sorted(d.items()))
for key, val in list(d.items()):
    print(key, val)
