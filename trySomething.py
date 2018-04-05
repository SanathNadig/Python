from collections import namedtuple

var = namedtuple('__CRC_PATCH_ADDR', 'name value')


from functools import reduce
from itertools import chain
from operator import add

class BigObject():
    pass

def namedtuplemerge(*args):
    print (args)
    cls = namedtuple('_'.join(arg.__class__.__name__ for arg in args), reduce(add, (arg._fields for arg in args)))
    return cls(*chain(*args))


def CustomizedEnum(_dict): 
    _all = [] 
    for key, val in _dict.items():
        obj = namedtuple(key, 'name value')
        obj.name = key
        obj.value = val
        setattr(newObj,key,obj)
        _all.append(obj)
#     return namedtuplemerge(tuple(_all))
    return newObj

newObj = BigObject()    
var = CustomizedEnum({'__Sanath':35, 'Pavithra':90})
print (var.__Sanath.value)
print ('done!')