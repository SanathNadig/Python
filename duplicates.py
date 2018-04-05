'''
a program to return the elements that are repeated in a list
'''

def check_for_duplicates(mylist):
    uniquelist = []
    duplicatelist = []
    for item in mylist:
        if not item in uniquelist:
            uniquelist.append(item)
        else:
            duplicatelist.append(item)
    print (duplicatelist)
          
mylist = [1,2,3,4,5,2,3,4]
check_for_duplicates(mylist)