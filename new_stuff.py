import mystuff

def number_info(number):
    """Assumes an integer and returns some info"""
    info = []
    if number % 2 == 0:
        info.append('even')
    else:
        info.append('odd')
    if mystuff.is_prime(number):
        info.append('prime')
    else:
        info.append('not prime')
    return "number is %s and %s" % (info[0], info[1])
