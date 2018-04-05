'''
using generators to retrieve the square of numbers upto a number n
'''
import random


def gensquares(N):
    for number in range(N):
        yield number**2
        
for x in gensquares(10):
    print (x)
    
    
def give_random_numbers(low,high,n):
    for _ in range(n):
        yield random.randint(low,high)
        

print ('\n\nthe random numbers are')        
for x in give_random_numbers(3, 100, 10):
    print (x)
    
s='hello'

gen_s = iter(s)