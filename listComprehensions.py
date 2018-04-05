'''
check for prime number
'''

def check_for_coprimes(num):
    mylist = [x for x in range(2,num) for i in range(1,x//2) if x%i != 0]
    print (mylist)
    
check_for_coprimes(50)
    
