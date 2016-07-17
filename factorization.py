#A program that factorizes a given number  -Shriram Krishnamachari 7/16/16
def smallestFactor(n):
    for i in range(2, n+1):
        if n % i == 0:
             return i
             
             
factor = list()

number = input('Give a number:')

if number == 1:
    factor.append(1)

cn = number
while cn > 1:
    sf = smallestFactor(cn)
    factor.append(sf)
    cn = cn / sf
    



factorstring = ''

if len(factor) > 1:
    for i in range(0, len(factor)- 1): 
        factorstring = factorstring + str(factor[i]) + ' x '
    factorstring = factorstring + str(factor[i+1])    
else:
    factorstring = str(factor[0])
    
print str(number) + ' = ' + factorstring












#####################################################
 
            
       
        
    
 

