a = 170
b = 170
c = 170
def summa (n1,n2):
    sum = n1+n2
    print sum
if  (a == b) or (b == c) or (a == c):
    print 'At least two numbers are equal. Correct the input'
elif a > b and b > c:
    num1 = a
    num2 = b
    summa (num1, num2)
elif a > b and c > b:
    num1 = a
    num2 = c
    summa (num1,num2)
else:
    num1 = b
    num2 = c
    summa (num1, num2)


