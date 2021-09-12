file = open(input('Enter a file name: '))
d = dict()
l = list()
for line in file:
    if line.startswith('From:'):
        word = line.split()
        try:
            d[word[1]] += 1
        except:
            d[word[1]] = 1
for key, val in list(d.items()):
    l.append((val, key))
l.sort(reverse = True)
print(l[0][1], l[0][0])
    
