# A program which shows a given amount of equally spaced numbers between
# 0 and another given number  -Shriram Krishnamachari 7/7/16

x = int(input("Enter Number: "))
n = int(input("How Many Numbers: "))

print str(n) + " equally spaced numbers between " + str(0) + " and " + str(x) + " are: "

for i in range(1, n+1):
    print i*(x/float(n+1))