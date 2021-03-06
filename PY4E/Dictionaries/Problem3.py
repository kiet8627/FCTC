file = open(input('Enter a file name: '))
cnt = dict()
name = str()
Max = int()
for line in file:
    if line.startswith('From:'):
        words = line.split()
        try:
            cnt[words[1]] += 1
        except:
            cnt[words[1]] = 1
        if Max is None or Max < cnt[words[1]]:
            name = words[1]
            Max = cnt[words[1]]
print(name, Max)
