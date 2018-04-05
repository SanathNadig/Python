st = 'Print only the words that start with s in this sentence'
stringList=st.split(' ')
print (stringList)
for word in stringList:
    if word[0]=='s' or word[0]=='S':
        print (word)
    
    
#code 2 begins here
#print every even number in 1 to 10 using list comprehension using range function
myEvenList=[num for num in range(0,11) if num%2==0]
print (myEvenList)


#code 3 here
#create a list of numbers from 1 to 50 that are divisible by 3
myNewList=[num for num in range(1,51) if num%3==0]
print (myNewList)


#code 4 here
st = 'Print every word in this sentence that has an even number of letters'
stringList=st.split(' ')
for word in stringList:
    if len(word)%2==0:
        print (word)
        
        
#code 5 here
st = 'Create a list of the first letters of every word in this string using list comprehension'
mylist=[word[0] for word in st.split(' ')]
print (mylist)

#Print only the words that start with s in this sentence
#method 2
st = 'Print only the words that start with s in this sentence'
mynewlist=[word for word in st.split() if word.startswith('s')]
print (mynewlist)