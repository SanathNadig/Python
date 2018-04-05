# problem on type error
for i in ['a','3','c']:
    try:
        print (i**2)
    except TypeError:
        print ('This action is not supported on this element.\nHave this instead. ')
        print (i*2)
        
# problem on ZeroDivisionError

x = 5
y = 0
try:
    print ('\n\nthe quotient is: {}'.format((x/y)))
except ZeroDivisionError:
    print ('\n\ndivision by zero is not possible')
finally:
    print ('All Done!\n\n')
    
def ask():
    while True:
        try:
            x = int(input('\nEnter an integer: '))
        except:
            print ('enter a valid number')
            continue
        else:
            print ('The square of the number is {}'.format(x**2))
            break

ask()