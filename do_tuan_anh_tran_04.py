#First part
#1
def capwords(s, sep=","):
    delimiters = [",", ".", "!", "?", "/n", "/", "&", "-", ":", ";", "@", "'", "..."]
    delimiters.remove(sep)
    new_s = s.title()
    for i in delimiters: 
        new_s = new_s.replace(i, ' ')
    return ' '.join(new_s.split())


#2 
def cut_suffix(word, suffix): 
    l_suffix = len(suffix)
    return word[:-3] if word.endswith(suffix) else word
    

#3 
def boxed(s, fill='*', pad=2):
    l_fill = len(s) + pad * 2 + 2 
    string_fill = fill * l_fill
    string_s = fill * pad + ' ' + s + ' ' + fill * pad
    result = f"""
{string_fill}
{string_s}
{string_fill} 
"""     
    return result 

#4 
def find_all(s, sub_s):
    l_sub = len(sub_s)
    position = []
    for n in range(len(s) - l_sub + 1):
        if s[n:n+l_sub] == sub_s:
            print('haha')
            position.append(n)
    return position

#5 
def common_prefix(*args):
    shortest = min(args, key=len)
    l_short = len(shortest)
    n_arg = len(args)
    longest_common = shortest
    for n in args:
        for i in range(l_short, 0, -1):
            if n[0:i] == shortest[0:i]:
                print('here')
                if len(longest_common) > i:
                    longest_common = n[0:i] 
                break
    return(longest_common)


#Second part 
#1 
def reader(a):
    return open(a)


#Third Part 
#1 
def words(s): 
    delimiters = [",", ".", "!", "?", "/n", "/", "&", "-", ":", ";", "@", "'", "..."]
    new_s = [x for x in s.split() if x not in delimiters]
    return new_s


#2
    