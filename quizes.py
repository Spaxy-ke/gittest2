print('quize 1:')
for i in range (5):
    print('*'*10)
print('quize 2:')
print('*'*10)
for i in range(3):
    print('*','*',sep='        ')
print('*'*10)
print('quize 3:')
for i in range(15):
    print('*'*(i+1))
print('quize 4:')
for i in range (5):
    print('*'*(5-i))
print('quize 5:')
'''quize 5 Ask the user to enter a number. Print out the square of the number, but use the sep optional
argument to print it out in a full sentence that ends in a period'''
n= eval(input('input a number:'))
print('the square of',n,'is',n*n,sep=' ',end='')
print('.',sep='')
print('quize 6:')
'''Ask the user to enter a number x . Use the sep optional argument to print out x , 2x , 3x , 4x ,
and 5x , each separated by three dashes'''
m= eval(input('enter a number:'))
print(m,2*m,3*m,4*m,5*m, sep='___')
print('quize 7:')
name1= input('enter your name:')
n2= eval(input('enter number of time you want your name to be displayed:'))
for i in range (n2):
    print((i+1),name1)
print('quize 8:')
sq1= eval(input('enter the last number:'))
print('square of numbers between 1 and',sq1,':')
for i in range (sq1):
    print((i+1),(1+i)*(1+i), sep='----')
print('quize 9:')
for i in range (8,90,3):
    print(i,end='  ')
print('')   
for j in range (90,20,-3):
    print(j,end='   ')
print('')
print('quize 10:')




