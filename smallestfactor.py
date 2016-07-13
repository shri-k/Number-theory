#A program that takes a given number and gives its smallest factor
#  -Shriram Krishnamachari 7/12/16


n=input('Enter a number')

for i in range(2, n+1):
    if n % i == 0:
        print 'The smallest factor of ' + str(n) + ' is ' + str(i)
        break