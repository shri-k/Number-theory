# Simple calculator: ask for two numbers, then ask which operation
#   then do it and give the answer.  -Shriram Krishnamachari 7/8/16

numb1 = input('Give a number:')
numb2 = input('Give another number:')
print "Which operation should I apply, add/subtract/multiply/divide"
op = raw_input('?')

if op == 'add':
    print str(numb1+numb2)
elif op == 'subtract':
    print str(numb1-numb2)
elif op == 'multiply':
    print str(numb1*numb2)
elif op == 'divide':
    print str(numb1/numb2)
else:
    print "Sorry I do not understand."