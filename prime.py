'''
check whether a given number is a prime Number
'''

def check_for_prime(num):
    for i in range(2,num//2):
        if num%i == 0:
            return False
    return True

print (check_for_prime(23))

'''
create a list of all coprimes of a Number
'''
def check_for_coprime(num):
    co_prime_list =[]
    if check_for_prime(num):
        co_prime_list = range(2,num)
    else:
        for i in range(2,num):
            if (check_num(i,num)):
                co_prime_list.append(i)
    print (co_prime_list)
    
def check_num(num,given_num):
    for i in range(2,num+1):
        if num%i ==0 and given_num%i ==0:
            return False
        
    return True

check_for_coprime(21)