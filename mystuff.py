def is_prime(number): # function to tell if a number is prime
    if number < 2: 
        return False
    else:
        for a in range(2, number): # remember indexing, range creates a list from 2 to number -1, [2,..,number-1]
            if number % a == 0: # if any number divides our number without remainder it's not prime.
                return False
    return True # it's got this far, so must be true.


def do_something():
    print "Doing something..."
    print "." * 30
    print "Still doing it"
    print "." * 30
    print "done"
    return "Need a break now"

    if __name__ == '__main__': # Do something will only run when called from command line, but not when imported.
        do_something()
