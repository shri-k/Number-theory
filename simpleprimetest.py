#A program that takes a given number and tells you whether it is 
#prime or composite. -Shriram Krishnamachari 7/9/16


n = input('Choose a number to test if it is prime:')


composite = None

for i in range(2, n):
    if n % i == 0:
        composite = True
        break

if composite == True:
    print str(n) + " is composite."
else:
    print str(n) + " is prime."
