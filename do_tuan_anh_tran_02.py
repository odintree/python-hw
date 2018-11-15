#PART 1

#1
def compose(f, g):
    return lambda x: f(g(x))

f = lambda x: x + 42
g = lambda x: x * x

h = compose(f, g)
h(2)

#2
def constantly(a):
    def func(*arg, **kwar): 
        return a
    return func

f = constantly(42)


 
#3
def func(x, y,  a="3", b=4):
    print(x)
    print(y)
    print(a)
    print(b)
    
def flip(func):
    def temp_func(*args):
        args = reversed(args)
        func(*args)
    return temp_func
    
    
flipped_func = flip(func)
flipped_func(1, 2,4)



#4
def func(x, y, z, a="4"):
    print(x)
    print(y)
    print(z)
    print(a)

def curry(func, a, x):
    def temp(*args):
        func(a,x,args[0])
    return temp

curried_func = curry(func, 1, 3)
print("NUMBER 4")
curried_func(2)


#PART TWO


#1
def enumerate1(a, start=0):
    theList = []
    #begin = start
    startPoint = start
    for i in a:
        theList.append((startPoint, i))
        startPoint += 1
    return theList        
   
    
#2
def which(a, b):
    theList = []
    for index, i in enumerate(b):
        if a(i):
            theList.append(index)
    return theList

xs = list(range(10, 20)) 
predicate = lambda x: x % 2 == 0
print(which(predicate, xs))

#3
def all(a, b):
    theList = []
    result = True 
    for i in b: 
        if not a(i):
            result = False
    return result

xs = list(range(10, 20)) 
predicate = lambda x: x % 2 == 0


#4
def any(a, b):
    theList = []
    result = False 
    for i in b: 
        if a(i):
            result = True
    return result



#PART THREEP


#1 

def char(a):
    def check(text):
        if not text:
            return ("ERROR", "eof", text)
        if a == text[0]:
            text = text[1:]
            return ("OK", a, text)
        else:
            return ("ERROR", f"expected {a} got {text[0]}", text)
    return check

#2 
def any_of(a):
    def check(text):
        if not text:
            return ("ERROR", "eof", text)        
        result = False
        for i in a:
            if i == text[0]: 
                result = True
        if result:
            return ("OK", text[0], text[1:])
        else:
            return ("ERROR", f"expected any of {a} got {text[0]}", text)
    return check




#3
def chain(*arg):
    def check(a):
        result = True
        positive = []
        negative = ""
        for i in arg:
            response = i(a)
            if response[0] == "OK": 
                positive.append(a[0])
                a = a[1:]
            if response[0] == "ERROR":
                result = False
                negative = response[1]
                break
        if result:
            return ("OK", positive, a)
        else:
            return ("ERROR", negative, a)
    return check


#4 
def choice(*arg):
    def check(a):
        if not a:
            return ("ERROR", "eof", a)       
        result = False
        positive = ""
        for i in arg:
            response = i(a)
            if response[0] == "OK": 
                positive = a[0]
                result = True
                break
            if response[0] == "ERROR":
                result = False
                negative = response[1]
                
        if result:
            return ("OK", positive, a)
        else:
            return ("ERROR", 'none matched', a)
    return check



#5
def many(func, empty=True):
    def check(a):
        if not a: 
            if not empty:
                return ("ERROR", "eof", a) 
            else:
                return ('OK', [], '')
        result = False
        positive = []
        negative = ""
        for i in a:
            response = func(i)
            if response[0] == "OK": 
                positive.append(a[0])
                a = a[1:]
                result = True
            if response[0] == "ERROR":
                negative = response[1]
                break                
        if result:
            return ("OK", positive, a)
        else:
            return ("ERROR", negative, a)
    return check
 


#6
def skip(func):
    def check(a):
        if not a:
            return ("ERROR", "eof", a)
        result = False
        negative = ""
        for i in a:
            response = func(i)
            if response[0] == "OK": 
                result = True
                a = a[1:]
            if response[0] == "ERROR":
                negative = response[1]
                break                
        if result:
            return ("OK", 'None', a)
        else:
            return ("ERROR", negative, a)
    return check
 

#7
def transform(func, func2):
    def check(a):
        if not a:
            return ("ERROR", "eof", a)
        result = False
        positive = ""
        for i in a:
            response = func(i)
            if response[0] == "OK": 
                result = True
                a = a[1:]
                positive = response[1]
            if response[0] == "ERROR":
                negative = response[1]
                break                
        if result:
            return ("OK", func2(positive), a)
        else:
            return ("ERROR", negative, a)
    return check


#8
def sep_by(func, sep):
    def check(a):
        if not a: 
            if not empty:
                return ("ERROR", "eof", a) 
            else:
                return ('OK', [], '')
        result = False
        positive = []
        negative = ""
        for index, i in enumerate(a):
            response = func(i)
            response2 = sep(i)
            if response2[0] == "OK":
                a = a[1:]
                continue
            if response[0] == "OK": 
                positive.append(a[0])
                a = a[1:]
                result = True
            if response[0] == "ERROR":
                negative = response[1]
                break
        if result:
            return ("OK", positive, a)
        else:
            return ("ERROR", negative, a)
    return check

#9