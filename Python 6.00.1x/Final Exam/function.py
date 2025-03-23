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

def uniqueValues(aDict):
    '''
    aDict: a dictionary
    returns: a sorted list of keys that map to unique aDict values, empty list if none
    '''
    # Your code here
    result = []
    values = list(aDict.values())
    for x,y in aDict.items():
        if values.count(y) <= 1:
            result.append(x)
    result.sort()
    return result

## DO NOT MODIFY THE IMPLEMENTATION OF THE Person CLASS ##
class Person(object):
    def __init__(self, name):
        #create a person with name name
        self.name = name
        try:
            firstBlank = name.rindex(' ')
            self.lastName = name[firstBlank+1:]
        except:
            self.lastName = name
        self.age = None
    def getLastName(self):
        #return self's last name
        return self.lastName
    def setAge(self, age):
        #assumes age is an int greater than 0
        #sets self's age to age (in years)
        self.age = age
    def getAge(self):
        #assumes that self's age has been set
        #returns self's current age in years
        if self.age == None:
            raise ValueError
        return self.age
    def __lt__(self, other):
        #return True if self's name is lexicographically less
        #than other's name, and False otherwise
        if self.lastName == other.lastName:
            return self.name < other.name
        return self.lastName < other.lastName
    def __str__(self):
        #return self's name
        return self.name
        
class USResident(Person):
    """ 
    A Person who resides in the US.
    """
    def __init__(self, name, status):
        """ 
        Initializes a Person object. A USResident object inherits 
        from Person and has one additional attribute:
        status: a string, one of "citizen", "legal_resident", "illegal_resident"
        Raises a ValueError if status is not one of those 3 strings
        """
        # Write your code here
        super().__init__(name)

        valid_status = ["citizen", "legal_resident", "illegal_resident"]
        if status in valid_status:
            self.status = status
        else:
            raise ValueError
        
    def getStatus(self):
        """
        Returns the status
        """
        # Write your code here
        return self.status
    
    



