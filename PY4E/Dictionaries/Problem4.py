file = open(input('Enter a file name: '))
cnt = dict()
for line in file:
    if line.startswith('From:'):
        words = line.split()
        for word in words:
            if '@' in word:
                try:
                    cnt[word[word.find('@') + 1 :]] += 1
                except:
                    cnt[word[word.find('@') + 1 :]] = 1
print(cnt)
