romannumbers = {9: 'IX', 5: 'V', 4: 'IV', 1: 'I'}
global one, two, three
one = 5
two = 4
three = 9
def roman(one, two):
    three = one + two
    rone = romannumbers.get(one)
    rtwo = romannumbers.get(two)
    rthree = romannumbers.get(three)
    print(rone, '+', rtwo, '=', rthree)
roman(one, two)
print(one, '+', two, '=', three)