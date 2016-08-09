#A function that takes two given numbers and finds their
#greatest common divisor  -Shriram Krishnamachari 7/18/16

from collections import Counter as mset

def smallestFactor(n):
    for i in range(2, n+1):
        if n % i == 0:
             return i


def factorize(number):
    factor = list()
    if number == 1:
        factor.append(1)
    cn = number
    while cn > 1:
        sf = smallestFactor(cn)
        factor.append(sf)
        cn = cn / sf
        
    return factor
        
        
        
def gcd(number1, number2):

	factor1 = factorize(number1)

	factor2 = factorize(number2)

	commonfactors =  list((mset(factor1) & mset(factor2)).elements())

	gcd = 1
	# the following loop takes each element in common factors
	# and makes gcd = gcd * e
	# the short form of which is gcd *= e
	for e in commonfactors: 
		gcd *= e
 
        return gcd 
