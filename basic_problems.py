import timeit

# Collection of GitHub Problems
# 1) Print factorial of a number:

def fact(x):
    if x == 0:
        return 1
    else:
        return x*fact(x - 1)

def input_to_fact():
    n = input('Enter your number: ')
    return fact(int(n))
    
# 2) For given n, create and display a dictionary with pairs (i, i^2) for 1 through to n

def dic_gen(x):
    dic = {}
    for i in range(1,x+1):
        dic[i] = i*i
    return dic

# we could also do this with dictionary comprehension (faster than for loop)

def dict_comp(x):
    return {i: i*i for i in range(1, x + 1)}

# time test
def wrapper(func, *args, **kwargs):
    def wrapped():
        return func(*args, **kwargs)
    return wrapped

def time_dicts(x):
    wrapped_gen = wrapper(dic_gen, x)
    wrapped_comp = wrapper(dict_comp, x)
    t1 = timeit.timeit(wrapped_gen, number=10000)
    t2 = timeit.timeit(wrapped_comp, number=10000)
    print('dic_gen took {} seconds; dict_comp took {} seconds'.format(t1, t2))

def input_to_dict():
    n = input('Please input your number: ')
    return dic_gen(int(n))

'''
# 3) Take in comma sep. numbers from console and display them in a list
list = []
x = input('Please enter a list of numbers, separated only by commas: ')

for i in x:
    if i != ',':
        list.append(i)

print(list)

#Better soln:

list_2 = []
list_2 = x.split(',')
tup = tuple(list_2)

print(list_2)
print(tup)

# 4) Make class with fns to take input, print, and test.

class baby_class:

    def get_input():
        x = input('Please type something: ')
        return x

    def print_shit_in_caps(a_string):
        caps = a_string.upper()
        print(caps)

# Look up wtf the __init__ method is, and why people care.
stuff = baby_class.get_input()
baby_class.print_shit_in_caps(stuff)


# 5) Import comma sep list of numbers, and finds their value after having been fed through a function, as a csl
from math import sqrt
x = input('Type a comma separated list of numbers: ')
output = []

ls = [i for i in x.split(',')]
print(ls)

for i in ls:
    output.append(str(float(sqrt((int(i)*30)/50))))

print(output)
print(','.join(output)) # don't convert to string here, it separates out every digit as a different value.

##############
multilist = [[i for i in [0,1,2,3,4,5]] for j in [1,2,'c']]

print(multilist)
##################


# 6) Take in comma sep. list of words, sort, return in c.s. string

x = input('Please enter a comma separated list of words: ')
x_new = x.split(',')
x_new.sort()

print(','.join(x_new))

# Take input from multiple lines, turn to caps, return
lines = []
Lines = []
while True:
    s = input('Please enter a line: ')
    if s:
        lines.append(s.upper())
    else:
        break

for stuff in lines:
    print(stuff)



# 7) Take in comma separated words, del repeated words, sort, return:

x = input('Please enter comma separated words: ')
x = x.split(',')

x.sort()
cnt = 0
while True:
    try:
        if x[cnt] == x[cnt+1]:
            del(x[cnt])
        else:
            cnt += 1
    except:
        break

print(','.join(x))
#or

x = input('Please enter comma separated words: ')
x = x.split(',')

#print(','.join(sorted(list(set(x)))))
print(','.join(set(x))) # SET() removes duplicates!
print(','.join(sorted(x)))

# 8) Take in list of 4-digit binary values, find and display any that are integers divisible by 5.

x = input('Please input 4-digit binary numbers, separated by commas: ')
x = x.split(',')
list = []
for nums in x:
    t = int(nums, 2)
    if not t%5:
        list.append(nums)

print(','.join(list))

# 9) / 10) Take in a string, and count the number of digits and letters, and display them.
# Also display how many of the letters were either upper or lower case.

x = input('Please enter a sentence: ')

dic = {'digits': 0, 'letters': 0}
no_upper, no_lower = 0, 0

for char in x:
    if char.isdigit():
        dic['digits'] += 1
    if char.isalpha():
        dic['letters'] += 1
        if char.isupper():
            no_upper += 1
        else:
            no_lower += 1
print('You\'ve entered',str(dic['digits']),'digits, and',str(dic['letters']),'letters.')
print(str(no_upper),'of the letters were in upper case, and the other',str(no_lower),'were in lower case.')

# 11) Get an int n as input and print and compute n + nn + nnn + nnnn where n is every digit in each number

x = input('Enter a number: ')

n1 = int( "%s" % x)
n2 = int( "%s%s" % (x,x))
n3 = int( "%s%s%s" % (x,x,x))
n4 = int( "%s%s%s%s" % (x,x,x,x))

print(n1 + n2 + n3 + n4)

# 12) Take in a list of ints separated by commas, and print the squares of each odd number.

x = input('Please enter a list of integers, separated by commas: ')

ints = [str(int(i)*int(i)) for i in x.split(',') if (int(i)%2 != 0)]

print(','.join(ints))

# 12) Take in strings of the form 'D 600' or 'W 700' (deposits or withdraws that debit or credit an amount),
# and compute the 'bank balance'.
tot = 0
while True:
    x = input('Please enter your transactions: ')
    x_list = [i for i in x.split(' ')]
    if x:
        if x_list[0] == 'D':
            tot += int(x_list[1])
        else:
            tot -= int(x_list[1])
        x_list = []
    else:
        break

print('Your bank balance is:',tot)

# 13) Check people's passwords.
# It has to have at least one small letter, one caps letter, one number, and one !@#$%^&*() length between 6 and 12,
# because fuck logic and expedience.

x = input('Please enter your stupid password: ')
letter, Letter, num, sign = 0,0,0,0

if not (6 <= len(x) <= 12):
    print('Your password is too big or too small.')
else:
    for i in range(len(x)):
        if x[i].isalpha():
            letter += 1
        if x[i].isupper():
            Letter += 1
        if x[i].isdigit():
            num += 1
        if x[i] in {'!','@','#','$','%','^','&','*','(',')'}:
            sign += 1

    if (letter >= 1) and (Letter >= 1) and (num >= 1) and (sign >= 1):
        print('You\'re good!')
    else:
        print('No man, do better!')'''

# or...
def pass_parse():
    import re # look up regular expressions!!! and this package.
    value = []
    items=[x for x in input('Please enter a bunch of passwords, separated by commas, because who knows why: ').split(',')]
    for p in items:
        if len(p) < 6 or len(p) > 12:
            continue
        else:
            pass
        if not re.search("[a-z]",p):
            continue
        elif not re.search("[0-9]",p):
            continue
        elif not re.search("[A-Z]",p):
            continue
        elif not re.search("[$#@]",p):
            continue
        elif re.search("\s",p):
            continue
        else:
            pass
        value.append(p)
    print('The reasonable passwords were: ',",".join(value))

