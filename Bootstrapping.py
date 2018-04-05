'''
Code to perform bootstrapping
'''
import random
def bootstrapping(lst,count):
    outer_list = []
    for _ in range(0,count):
        inner_list = []
        for _ in range(0,len(lst)):
            inner_list.append(random.choice(lst))
        outer_list.append(inner_list)
    print (outer_list)
    
mylist = [1,2,3,4,5,6,7,8,9,10]
bootstrapping(mylist,10)


