def main():
    mystr='hello world'
    print(mystr)
    newstr=mystr.capitalize()
    print('The disintegrated string is {}'.format(mystr[1:]))
    print (newstr)
    print (mystr+'\t' + newstr)
    splitstr=mystr.split('l')
    print (splitstr)
    num=37043.641646
    print('the number is {n:4.5f}'.format(n=num))
    myList=[1,2,3,4,5,6,7,8]
    print (myList[7:3:-1])
    myDict={'key1':100,'key2':200,'key3':300}
    print (myDict)
    myDict['key3']=350
    print(myDict)
    myDict['key4']=400
    print(myDict)
    print (len(myDict))
    
    mytuple=(1,2,[1,2])
    print(mytuple)
    print(mytuple[2])
    print(mytuple[2][1])
    mytuple[2][1]=5
    print(mytuple)
    
    
if __name__=="__main__":
    main()
    