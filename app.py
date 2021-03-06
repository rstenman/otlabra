#!/usr/bin/python
import sys

# Implementation of FizzBuzz v0.00

# Version 1: if number is divisible by 3, print Fizz
#            if number is divisible by 5, print Buzz
#            if both, print FizzBuzz
#            else print number

# Version 2: if number is prime, print "<number> is a prime" instead
#            Take one argument,  and count up to it

class FizzBuzz():
    def __init__(self):
        pass

    # Run from 1 to "end". Maybe. Test fails for some reason
    def run(self, end, out=sys.stdout):
        for i in range(1, end +1):
            print >> out, self.calc(i)

    # Seems to give correct values. Tested with 1 and 2.
    def calc(self, i):
        j = "Fizz"
	k = "Buzz"	
	if (i % 3 == 0 and i % 5 == 0):
	    return j+k
	elif (i % 3 == 0):
	    return j
	elif (i % 5 == 0): 
	    return k
        else:    	
            return i

if __name__ == "__main__":
    app = FizzBuzz()
    app.run(100)
