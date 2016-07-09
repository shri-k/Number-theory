#A program that asks the user which times table they want
#   and prints it  -Shriram Krishnamachari 7/8/16

Number = input('Which times table should I display: ')
for i in range(1, 11):
    print str(Number) + " x " + str(i) + " = " + str(Number*i)