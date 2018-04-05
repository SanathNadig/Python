fibo=[0,1]
total_even=0
while fibo[-1]<4000000:
    fibo.append(fibo[-1]+fibo[-2])
    if fibo[-1]%2==0:
        total_even+=fibo[-1]
else:
    fibo.pop()
print ('the sum of even nos is {}.'.format(total_even))
print ('last number is {}'.format(fibo[-1]))