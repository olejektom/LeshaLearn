digits = [9999, 342, 41,55,74, 42,148,42]
for digit in digits:
    if digit == 42:
        print ('The Answer to the Ultimate Question of Life, the Universe, and Everything')
        break
    elif digit/100 == 0:
        print digit