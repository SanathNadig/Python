'''
def lesser_of_two_events(num1,num2):
    if num1%2==0 and num2%2==0:
        return(num1) if num1<=num2 else return(num2)
    else:
        return num1 if num1>=num2 else return num2
    
answer=lesser_of_two_events(2,5)
print ("answer of (2,5) is: " + answer )
answer=lesser_of_two_events(2, 4)
print ("answer of (2,4) is: " + answer )
'''
import math
import string
#makes twenty
def makes_twenty(num1,num2):
    return (num1==20) or (num2==20) or (num1+num2==20)

answer=makes_twenty(11, 10)
print(answer)

#old macdonald
def old_macdonald(name):
    newname = name.capitalize()
    newname = newname.replace(newname[3],newname[3].upper())
    print (newname)
    
old_macdonald('sanath')


#master yoda

def master_yoda(mystring):
    mylist=mystring.split(' ')
    mylist.reverse()
    mynewstring=' '.join(mylist)
    return mynewstring

answer=master_yoda('hi i am sanath')
print (answer)

#find 33

def has_33(testlist):
    for i in range(1,len(testlist)):
        if (testlist[i]==testlist[i-1]==3):
            return True
    return False
    
print(has_33([4,3,3]))


#paper doll
def paper_doll(word):
    newword=[letter*3 for letter in word]
    return ''.join(newword)
print(paper_doll('Mississippi'))


#blackjack
def blackjack(n1,n2,n3):
    total=n1+n2+n3
    if total<=21:
        return total
    elif 11 in [n1,n2,n3]:
        return total-10
    else:
        return 'BUST'

print(blackjack(9,9,11))


#summer of 69
def summer_69(arr):
    total_sum = 0
    Flag=False
    for num in arr:
        if num == 6:
            Flag=True
        if arr[arr.index(num)-1] == 9:
            Flag=False
        if not Flag:
            total_sum += num
    return total_sum    
            
        

print(summer_69([2, 1, 6, 9, 11]))

#count of primes
def count_primes(num):
    mylist=[]
    for x in range(2,num+1):
        flag=True
        for i in range(2,x//2+1):
            if x%i==0:
                flag=False
                break
        if flag:
            mylist.append(x)
    print (mylist)
    return len(mylist)


print(count_primes(100))

#spy gane
def spygame(nums):
    count=0
    for num in nums:
        if num==0 and count == 0:
            count +=1
            continue
        if num==0 and count == 1:
            count +=1
            continue
        if num ==7 and count ==2:
            count +=1
            continue
    print ('count value is {}'.format(count))
    return (count==3)

print (spygame([1,7,2,0,4,5,0]))
    
    
    
#volume of a sphere
def vol(rad):
    return ((4/3.0)*math.pi*(rad**3))
print (vol(2))

#upper and lower case letters

def up_low(s):
    upcount = 0
    lowcount = 0
    for letter in s:
        if letter.isupper():
            upcount += 1
        elif letter.islower():
            lowcount += 1
    print('number of upper case letters is {u} \nnumber of lower case letters is {l}'.format(u=upcount,l=lowcount))
    
up_low('Hello Mr. Rogers, how are you this fine Tuesday?')

#unique list
def unique_list(mylist):
    return set(mylist)

myset=unique_list([1,1,1,1,2,2,3,3,3,3,4,5])
print (myset)

#is pangram
def ispangram(mystr, alphabet=string.ascii_lowercase):
    alphaList=[letter for letter in alphabet]
    return set(mystr.lower().replace(' ', '')) == set(alphaList)
    
print (ispangram('The quick brown fox jumps over the lazy dog'))

            