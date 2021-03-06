file = open(input('Enter a file name: '))
cnt = dict()
for line in file:
    if line.startswith('From'):
        word = line.split()
        if len(word) > 2:
            try:
                cnt[word[2]] += 1
            except:
                cnt[word[2]] = 1
print(cnt)
