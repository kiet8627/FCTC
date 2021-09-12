total = 0
count = 0
inp = 0
while inp != 'done':
    inp = input('Enter a number: ')
    try:
        inp = int(inp)
        total += inp
        count += 1
    except:
        if inp != 'done':
            print('Invalid input')
print(total, count, total / count)
