'''
code to demonstrate the use of decorators.
'''
import time

def timer(originalfunc):
    
    def wrapper(*args):
        start_time = time.clock()
        print (args)
        result = originalfunc(*args)
        print (time.clock() - start_time)
        return result
    return wrapper

@timer
def myfunc():
    for i in range(100000):
        i+=1
    print (i)



if __name__ == "__main__":
    print (myfunc)
    myfunc()
    