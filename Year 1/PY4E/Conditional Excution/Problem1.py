hour = float(input('Enter Hours: '))
rate = float(input('Enter Rate: '))
if hour > 40: print('Pay:', 40 * rate + (hour - 40) * 10 * 1.5)
else: print('Pay:', hour * rate)
