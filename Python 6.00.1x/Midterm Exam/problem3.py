def myLog(x, b):
    '''
    x: a positive integer
    b: a positive integer; b >= 2

    returns: log_b(x), or, the logarithm of x relative to a base b.
    '''
    logarithm = 0
    while b ** logarithm <= x:
        logarithm += 1
    
    return logarithm

def lessThan4(aList):
    '''
    aList: a list of strings
    '''
    # Your code here