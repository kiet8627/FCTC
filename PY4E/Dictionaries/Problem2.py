file = open(input('Enter file name: '))
cnt = dict()
for line in file:
    if not line.startswith('From:'):
        continue
    word = line.split()
    try:
        cnt[word[1]] += 1
    except:
        cnt[word[1]] = 1
print(cnt)
