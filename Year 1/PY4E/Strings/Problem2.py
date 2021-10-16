inp = input()
while inp != '0':
    num = int(inp[: inp.find(' ')])
    s = inp[inp.find(' ') + 1 :]
    _s = ''
    for c in s:
        c = chr(ord('A') + (ord(c) + num - ord('A')) % 26)
        _s += c
    print(_s[:: -1])
    inp = input()
