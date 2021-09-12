def computepay(hour, rate):
    if hour > 40: return 40 * rate + (hour - 40) * 10 * 1.5
    else: return hour * rate

hour = float(input('Enter Hours: '))
rate = float(input('Enter Rate: '))
print('Pay:', computepay(hour, rate))
