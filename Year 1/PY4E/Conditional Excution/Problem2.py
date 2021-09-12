hour = input('Enter Hours: ')
try:
    hour = float(hour)
    rate = input('Enter Rate: ')
    try:
        rate = float(rate)
        if hour > 40: print('Pay:', 40 * rate + (hour - 40) * 10 * 1.5)
        else: print('Pay:', hour * rate)
    except:
        print('Error, please enter numeric input')
except:
    print('Error, please enter numeric input')
