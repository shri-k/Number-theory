#A program that takes two fractions and adds them
#-Shriram Krishnamachari 8/9/16

from gcd import gcd

print('This program will calculate the addition of two fractions')

a = input('Give the numerator of the first number: ')
b = input('Give the denominator of the first number: ')
c = input('Give the numerator of the second number: ')
d = input('Give the denominator of the second number: ')

e =  a*d + b*c
f =  b*d
g = gcd(e, f)

print ("The answer is: "+str(e/g)+"/"+str(f/g))
