from collections import namedtuple


class DH():
    def __init__(self):
        pass
    
    def get_attr_name(self,attr_name):
        return getattr(self, attr_name)
    
    
    
def CustomizedEnum(_dict):
    import re
    data_holder= DH()
    for key, val in _dict.items():
        obj = namedtuple(key, 'name value')
        obj.name = key
        obj.value = val
#         if key.startswith('__'):
#             key = re.sub("__", "",  key, count=1)
#             key = 'DOUBLE_UNDERSCORE_' + key
        setattr(data_holder, key, obj)
    return data_holder 

# var = CustomizedEnum({'__CRC_PATCH_ADDR':'00000000', '__PCODE_END':'DEADBEEF'}) 
# print (var.__CRC_PATCH_ADDR.name)

class sample:
    def __init__(self):
        self.ex = None

    def samp(self):
        self.ex = CustomizedEnum({'__CRC_PATCH_ADDR':'00000000', '__PCODE_END':'DEADBEEF'})
        print (self.ex.__CRC_PATCH_ADDR)
            
a = sample()
a.samp()