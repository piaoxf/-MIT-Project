def print_without_vowels(s):
    '''
    s: the string to convert
    Finds a version of s without vowels and whose characters appear in the 
    same order they appear in s. Prints this version of s.
    Does not return anything
    '''
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    result = ''
    for c in s:
        if c in vowels:
            continue
        result += c
    
    print(result)


def longest_run(L):
    """
    Assumes L is a list of integers containing at least 2 elements.
    Finds the longest run of numbers in L, where the longest run can
    either be monotonically increasing or monotonically decreasing. 
    In case of a tie for the longest run, choose the longest run 
    that occurs first.
    Does not modify the list.
    Returns the sum of the longest run. 
    """
    increasing = {}
    decreasing = {}

    # increasing k+1 >= k decreasing k >= k+1
    i = 0
    while i < len(L):
        value = [L[i]]
        increasing[i] = value
        
        for e in L[i+1:]:
            if e >= L[i]:
                value.append(e)
                i +=1
            else:
                break
        i += 1
    
    i = 0
    while i < len(L):
        value = [L[i]]
        decreasing[i] = value
        
        for e in L[i+1:]:
            if e <= L[i]:
                value.append(e)
                i +=1
            else:
                break
        i += 1

    inc_start = 0
    inc_max = 0
    dec_start = 0
    dec_max = 0
    for x,y in increasing.items():
        if len(y) > inc_max:
            inc_start = x
            inc_max = len(y)
    for x,y in decreasing.items():
        if len(y) > dec_max:
            dec_start = x
            dec_max = len(y)
    result = 0
    if inc_max > dec_max:
        result = sum(increasing[inc_start])
    elif inc_max < dec_max:
        result = sum(decreasing[dec_start])
    else:
        if inc_start < dec_start:
            result = sum(increasing[inc_start])
        elif inc_start > dec_start:
            result = sum(decreasing[dec_start])
        else:
            result = sum(increasing[inc_start])
    return result

    
    



