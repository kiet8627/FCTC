Max = - 10 ** 999
Min = 10 ** 999
inp = 0
while inp != 'done':
    inp = input('Enter a number: ')
    try:
        inp = int(inp)
        Max = max(Max, inp)
        Min = min(Min, inp)
    except:
        if inp != 'done':
            print('Invalid input')
print('Maximum: ', Max)
print('Minimum: ', Min)
