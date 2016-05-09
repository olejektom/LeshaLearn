

def summed_digits (*args):
    summa = 0
    for arg in args:
        while arg > 0:
            a=arg%10
            summa = summa + a
            arg=arg/10
    print summa

summed_digits (35,30,11,101,1001)