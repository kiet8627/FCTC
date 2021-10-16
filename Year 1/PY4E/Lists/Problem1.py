file_name = input('Enter file: ')
file = open(file_name)
kq = []
for line in file:
    words = line.split()
    for word in words:
        if word not in kq:
            kq.append(word)
kq.sort()
print(kq)
