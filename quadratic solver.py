'''This program helps you solve quadratic equation using 
 the quadratic formula principle
 
Quadratic formula, x = -b +- sqrt(b^2 - 4ac)/2a 
'''

from math import sqrt


try:
    a = int(input('Input the value of a: '))
    b = int(input('Input the value of b: '))
    c = int(input('Input the value of c: '))

    numeratorA = (-b) + sqrt((b*b)-(4*a*c))
    numeratorB = (-b) - sqrt((b*b)-(4*a*c))

    denominator = 2 * a

    root1 = numeratorA/denominator
    root2 = numeratorB/denominator

    print('The roots are:', root1, "and", root2)
except:
    print('Enter only numbers!')

    

