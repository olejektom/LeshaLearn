def even_odd (a):
    for number in a:
        if number%2==0:
            number = str(number)
            print 'An even number:'+number
        else:
            number = str(number)
            print 'An odd number:'+number

even_odd ([2,4,5,6,7,8,11])
