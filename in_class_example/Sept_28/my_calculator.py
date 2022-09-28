import math

# def sqrt(input):
#     return math.sqrt(input)



def sqrt(n):
    print(type(n))
    if n<0:
        raise ValueError('sqrt received a value < 0')
    if type(n) == str:
        raise TypeError('Cannot send stringn')
    x = n
    y = 1

    e = 0.00000001
    while (x-y > e):
        x = (x+y)/2
        y=n/x

    return x