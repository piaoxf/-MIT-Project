import function as fun

# print_without_vowels(s)
# s = "This is great!"
# fun.print_without_vowels(s)
# s = "a"
# fun.print_without_vowels(s)


# longest_run(L)
# L = [10, 4, 3, 8, 3, 4, 5, 7, 7, 2]
# fun.longest_run(L)
# L = [5, 4, 10]
# fun.longest_run(L)

# uniqueValues(aDict)
# aDict = {1: 1, 3: 2, 6: 0, 7: 0, 8: 4, 10: 0}
# print(fun.uniqueValues(aDict))
# aDict = {1: 1, 2: 1, 3: 1}
# print(fun.uniqueValues(aDict))

# USResident
# a = fun.USResident('Tim Beaver', 'citizen')
# print(a.getStatus())
# b = fun.USResident('Tim Horton', 'non-resident')

# ASet(Container)
d1 = fun.ASet()
d1.insert(4)
d1.insert(4)

d1.remove(2)
print(d1)

d1.remove(4)
print(d1)

d1 = fun.ASet()
d1.insert(4)
print(d1.is_in(4))
d1.insert(5)
print(d1.is_in(5))
d1.remove(5)
print(d1.is_in(5))