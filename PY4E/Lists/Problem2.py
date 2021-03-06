file_name = input('Enter a file name: ')
file = open(file_name)
num_lines = 0
for line in file:
    if not line.startswith('From'):
        continue
    num_lines += 1
    words = line.split()
    print(words[1])
if num_lines == 1:
    print('There was 1 lines in the file with From as the first word')
else:
    print('There were', num_lines, 'lines in the file with From as the first word')
