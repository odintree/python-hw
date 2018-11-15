import functools

#Part1
#1
def union(*args):
    lst = []
    for arg in args:
        for i in arg:
            lst.append(i)
    result = set(lst)
    return result


#2
def digits(number):
    if number < 0: 
        return "I NEED non-negative number"
    result = []
    strNumber = str(number)
    for n in strNumber:
        result.append(int(n))
    return result



#3
def lcm_two_numbers(a, b):
   if a > b:
       c = a
   else:
       c = b
   while(True):
       if((c % a == 0) and (c % b == 0)):
           lcm = c
           break
       c += 1
   return lcm

def lcm(*args):
    return functools.reduce(lambda x, y: lcm_two_numbers(x, y), args)

#4
def compose (*funcs):
    def temp_func(arg):
        for f in reversed(funcs):
            arg = f(arg)
        return arg
    return temp_func

#Part2 
#1
def once(func):
    def inner(*args, **kwargs):
        if not inner.cached:
            inner.value = func(*args, **kwargs)
            inner.cached = True
        return inner.value
    inner.cached = False

    return functools.update_wrapper(inner, func)
@once
def kak(b):
    print('something something')
    return b 
kak(7)
kak(7)
#2


#3
def n_times(n):
    def decorate(function):
        def another(*args):
            for x in range(n):
                function(*args)
        return another
    return decorate
        