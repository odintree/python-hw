from collections import namedtuple
from collections import OrderedDict
from collections import defaultdict

import functools


#PART ONE
#1 
def factor(a):
    unique = []
    [unique.append(i) for i in a if i not in unique]
    finalDict = {}
    for index, i in enumerate(unique):
        finalDict[i] = index
    newList = list(map(lambda x: finalDict[x], a))
    Factor = namedtuple("Factor", ["elements", "levels"])
    f = Factor(newList, OrderedDict(finalDict))
    return f
    
#2 


# Taken from http://code.activestate.com/recipes/578078
# A 2.6.x backport of Python 3.3 functools.lru_cache
#
# Modified from 4=>2 length indents for code consistency.
#
# Added an on_eviction parameter that gets applied to each element
# when it is evicted from the cache, e.g. file.close(...).


def lru_cache(func, maxsize=64):
    def inner(x):
        if not inner.cached:
            inner.value = func(x)
            inner.cached = True
            inner.dict[x] = inner.value
        if x in inner.dict:
            inner.hit += 1 
            inner.value = inner.dict[x]
        else: 
            inner.missed += 1
            inner.value = func(x)
            if len(inner.dict) > maxsize:
                inner.dict.popitem(last=False)
                inner.dict[x] = inner.value
        return inner.value
    inner.cached = False
    inner.missed = 0
    inner.hit = 0 
    inner.dict = OrderedDict()
    def cache_info():
        CacheInfo = namedtuple("CacheInfo", ["hits", "misses", "maxsize", "currentsize"])
        ci = CacheInfo(inner.hits, inner.missed, maxsize, len(inner.dict))
        return ci
    return functools.update_wrapper(inner, func)
    def cache_clear():
        inner.cached = False
        inner.missed = 0
        inner.hit = 0 
        inner.dict.clear()


#3
def group_by(lst, func):
    final = {}
    for i in lst:
        if func(i) in final:
            final.setdefault(func(i), []).append(i)
        else: 
            final[func(i)] = [i]
    return OrderedDict(final)


#4 
def invert(slov):
    newKey = set(slov.values())
    newDict = dict.fromkeys(newKey, {})
    for key, value in slov.items():
        if len(newDict[value]):
            newDict[value].add(key)
        else: 
            newDict[value] = {key}
    return newDict


print(invert({"a": 42, "b": 42, "c": 24}))