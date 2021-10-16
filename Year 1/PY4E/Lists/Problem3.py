a = []
while True:
    inp = input('Enter a number: ')
    if inp == 'done':
        break
    a.append(int(inp))
print('Maximum:', max(a))
print('Minimun:', min(a))
