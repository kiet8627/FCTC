from math import tan
from math import pi
def polysum(n, s):
    a = (n * s * s) / (4 * tan(pi / n))
    p = s * n
    return round(a + p * p, 4)
